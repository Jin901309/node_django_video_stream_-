#지원 되는 확장자만 파일 업로드
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    #원하는 확장자 명
    valid_extensions = ['.mp4','.avi', '.wmv', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')