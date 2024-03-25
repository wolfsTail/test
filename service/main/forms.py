from django import forms


class FileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data["file"]

        if file.content_type != "text/plain":
            raise forms.ValidationError("Для анализа допустимы только текстовые файлы (.txt)!")
        
        return file