

import os
import time

def initSeparator(separator_params):
    start_time = time.time()
    from spleeter.separator import Separator

    filename = separator_params['filename']
    file_directory = separator_params['foldername']

    print('---> processing '+ filename)
    separator = Separator(separator_params['stems'])
    codec=separator_params['codec']
    separator.separate_to_file(filename, file_directory, codec=codec, synchronous=False)
    separator.join()
    finish_time = time.time()
    total = finish_time - start_time

    print('---> Process finished in  '+ str(total))
    print('---> Files added to '+ file_directory)
    print('---> Finishing program...')

    separator._get_session().close()

    os.startfile(file_directory)

    return True

