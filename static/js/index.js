document.addEventListener('DOMContentLoaded', function() {
    var deleteButton = document.getElementById('delete-button');
  
    function updateDeleteButtonVisibility() {
      var selectedThumbnails = document.querySelectorAll('.thumbnail.selected');
      deleteButton.style.display = selectedThumbnails.length > 0 ? 'block' : 'none';
    }
  
    // クリックで選択状態を切り替える
    document.querySelectorAll('.thumbnail').forEach(function(thumbnail) {
      thumbnail.addEventListener('click', function() {
        this.classList.toggle('selected');
        updateDeleteButtonVisibility();
      });
    });
  
    // 削除ボタンが押されたときの処理
    deleteButton.addEventListener('click', function() {
      var selectedImages = Array.from(document.querySelectorAll('.thumbnail.selected')).map(function(thumbnail) {
        return thumbnail.querySelector('img').alt;
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
    var totalFileSize = 0;
    for (var i = 0; i < input.files.length; i++) {
        totalFileSize += input.files[i].size; // size in bytes
    }
    // Convert size to MB
    totalFileSize = totalFileSize / 1024 / 1024;
    if (totalFileSize > 100) {
        alert("合計ファイルサイズは100MBまでです");
        input.value = ""; // Clear the selection
    } else {
    input.form.doSubmit.click()
    }
}
