'''
https://docs.python.org/3/library/configparser.html
'''
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print(config['APP']['NUMBER'])
print(config['DB']['HOST'])
print(config['DB']['USERNAME'])
print(config['DB']['PASSWORD'])