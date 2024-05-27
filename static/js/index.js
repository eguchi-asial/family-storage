document.addEventListener('DOMContentLoaded', function() {
    const selectButton = document.querySelector('#select-button');
    const cancelButton = document.querySelector('#cancel-button');
    const deleteButtonArea = document.querySelector('.delete-area');
    const thumbnails = document.querySelectorAll('.thumbnail');

    selectButton.addEventListener('click', function() {
        cancelButton.style.display = 'block';
        const checkboxes = document.querySelectorAll('.image-checkbox');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
            checkbox.style.display = 'block'
        });
    });

    thumbnails.forEach(function(thumbnail) {
        thumbnail.addEventListener('click', function(e) {
            // チェックボックスのchangeイベントと重複してしまうため、ここで処理を分岐
            if (e.target.nodeName === 'IMG') {
                thumbnail.classList.toggle('selected');
                // キャンセルボタンが表示されていない＝編集モードではない場合
                if (cancelButton.style.display !== 'block') {
                    // Get the original image URL
                    let originalImageUrl = e.target.src.replace('thumbnail/thumbnail_', '/');
                    // Check if the file extension is '.png'
                    if (originalImageUrl.endsWith('_movie.png')) {
                        // data-original属性の値を取得し、拡張子を抽出してセット
                        const originalDatasetValue = e.target.dataset.original;
                        originalImageUrl = originalImageUrl.replace('_movie.png', '.' + originalDatasetValue.split('.').pop());
                    }

                    // ファイル拡張子を取得
                    const fileExtension = originalImageUrl.split('.').pop();

                    // 動画ファイルの拡張子のリスト
                    const videoExtensions = ['mp4', 'mov', 'avi', 'mpg', 'mpeg']

                    // Create a new div element for the popup background
                    const popupBackground = document.createElement('div');
                    popupBackground.style.position = 'fixed';
                    popupBackground.style.top = '0';
                    popupBackground.style.left = '0';
                    popupBackground.style.width = '100vw';
                    popupBackground.style.height = '100vh';
                    popupBackground.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
                    popupBackground.style.display = 'flex';
                    popupBackground.style.justifyContent = 'center';
                    popupBackground.style.alignItems = 'center';
                    popupBackground.style.zIndex = '1000';

                    // originalImageUrlが動画ファイルであるかチェック
                    if (videoExtensions.includes(fileExtension)) {
                        // Create a new video element for the popup
                        const popupVideo = document.createElement('video');
                        popupVideo.src = originalImageUrl;
                        popupVideo.controls = true;
                        popupVideo.style.maxWidth = '90vw';
                        popupVideo.style.maxHeight = '90vh';
                        popupVideo.style.zIndex = '1100';
                        popupVideo.addEventListener('click', function(e) {
                            e.stopPropagation();
                        });

                        // Add the video to the popup background
                        popupBackground.appendChild(popupVideo);
                    } else {
                        // Create a new image element for the popup
                        const popupImage = document.createElement('img');
                        popupImage.src = originalImageUrl;
                        popupImage.style.maxWidth = '100vw';
                        popupImage.style.maxHeight = '100vh';

                        // Add the image to the popup background
                        popupBackground.appendChild(popupImage);
                    }

                    // Add the popup background to the body
                    document.body.appendChild(popupBackground);

                    // Remove the popup when the background is clicked
                    popupBackground.addEventListener('click', function() {
                        document.body.removeChild(popupBackground);
                    });
                }
            }
        });

        const checkbox = thumbnail.querySelector('.image-checkbox');
        checkbox.addEventListener('change', function(e) {
            e.stopPropagation();
            console.log('change')
            if (checkbox.style.display !== 'block') return
            if (this.checked) {
                thumbnail.classList.add('selected');
            } else {
                thumbnail.classList.remove('selected');
            }
            const selectedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
            if (selectedCheckboxes.length > 0) {
                deleteButtonArea.style.display = 'block';
            } else {
                deleteButtonArea.style.display = 'none';
            }
        });
    });

    cancelButton.addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(function(checkbox) {
            checkbox.checked = false;
            checkbox.style.display = 'none';
        });
        deleteButtonArea.style.display = 'none';
        cancelButton.style.display = 'none';
    });
  
    // 削除ボタンが押されたときの処理
    deleteButtonArea.addEventListener('click', function() {
      const selectedImages = Array.from(document.querySelectorAll('.thumbnail.selected')).map(function(thumbnail) {
        return thumbnail.querySelector('img').getAttribute('data-original');
      });
  
      fetch('/delete', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(selectedImages),
      }).then(function(response) {
        if (response.ok) {
          // 削除が成功したら画面をリロード
          location.reload();
        } else {
          console.error('Failed to delete images');
        }
      });
    });
});

function checkFileSize(input) {
    let totalFileSize = 0;
    for (let i = 0; i < input.files.length; i++) {
        totalFileSize += input.files[i].size; // size in bytes
    }
    // Convert size to MB
    totalFileSize = totalFileSize / 1024 / 1024;
    if (totalFileSize > 500) {
        alert("合計ファイルサイズは500MBまでです");
        input.value = ""; // Clear the selection
    } else {
    input.form.doSubmit.click()
    }
}
