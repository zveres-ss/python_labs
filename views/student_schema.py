from myapp import ma

class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('first_name', 'last_name')
