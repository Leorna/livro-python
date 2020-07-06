import traceback


try:
    raise Exception('This is the error message.')
except:
    with open('errors.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print('The traceback info was written to errors.txt.')