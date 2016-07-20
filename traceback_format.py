import traceback

try:
    raise Exception('This is the error message.')
except:
    error_file = open('errorInfo.txt', 'w')
    print(error_file.write(traceback.format_exc()))
    error_file.close()
    print('The traceback info was written to errorInfo.txt.')
