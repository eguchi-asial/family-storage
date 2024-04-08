from flask import render_template, request, redirect
from __init__ import app
import logging

# services
from services.thumbnail_service import get_thumbnail_files
from services.upload_service import upload_files
from services.delete_service import delete_files as delete_service

@app.route('/')
def index():
    thumbnail_files = get_thumbnail_files()
    return render_template('index.html', image_files=thumbnail_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('file')
    success, error = upload_files(files)
    if not success:
        logging.warning(error)
        return redirect('/')
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_files():
    files_to_delete = request.get_json()
    delete_service(files_to_delete)
    return '', 204
