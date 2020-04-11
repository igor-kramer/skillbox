import uuid
from django import forms
from .models import Link


class CreateLinkForm(forms.ModelForm):
     
    class Meta:
        model = Link
        fields = ('url',)

    def save(self, commit=True):
        while True:
            uid = str(uuid.uuid4())
            uid = uid.replace('-', '')[:8]
            if not Link.objects.filter(id=uid).exists():
                break

        link = super(CreateLinkForm, self).save(commit=False)
        link.id = uid
        link.save()
        return link
        