import sys

from django.shortcuts import render

# Create your views here.


def index(req):
    """
    :param req:
    :return:
    """
    return render(req, 'index.html')


def execute_code(req):

    first_stdout = None
    code_field_data = None
    output = None

    if req.method == 'POST':
        code_field_data = req.POST['code_field']

        try:
            # Write stdout to a temp file.
            first_stdout = sys.stdout
            sys.stdout = open('tempfile.txt', 'w')

            # Execute code.
            exec(code_field_data)

            sys.stdout.close()
            sys.stdout = first_stdout

            output = open('tempfile.txt', 'r').read()
        except Exception as error:
            output = error
            sys.stdout = first_stdout

    # Return and render data to output.
    return render(req, 'index.html', {'code_data': code_field_data, 'output': output})



