document.addEventListener('DOMContentLoaded', function() {
    const selectButton = document.getElementById('select-button');
    const cancelButton = document.getElementById('cancel-button');
    const deleteButton = document.getElementById('delete-button');
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
        thumbnail.addEventListener('click', function() {
            thumbnail.classList.toggle('selected');
        });

        const checkbox = thumbnail.querySelector('.image-checkbox');
        checkbox.addEventListener('change', function() {
            if (checkbox.style.display !== 'block') return
            if (this.checked) {
                thumbnail.classList.add('selected');
            } else {
                thumbnail.classList.remove('selected');
            }
            const selectedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
            if (selectedCheckboxes.length > 0) {
                deleteButton.style.display = 'block';
            } else {
                deleteButton.style.display = 'none';
            }
        });
    });

    cancelButton.addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(function(checkbox) {
            checkbox.checked = false;
            checkbox.style.display = 'none';
        });
        deleteButton.style.display = 'none';
        cancelButton.style.display = 'none';
    });
  
    // 削除ボタンが押されたときの処理
    deleteButton.addEventListener('click', function() {
      const selectedImages = Array.from(document.querySelectorAll('.thumbnail.selected')).map(function(thumbnail) {
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
    let totalFileSize = 0;
    for (let i = 0; i < input.files.length; i++) {
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
