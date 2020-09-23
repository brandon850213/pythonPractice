from translate import Translator

try:
    with open('./beforeTranslate.txt', mode = 'r') as my_file:
        text = my_file.read()
        translator= Translator(to_lang="de")
        translation = translator.translate(text)
        with open('afterTranslate.txt', mode = 'w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('Enter a valid file path!')
    raise err
