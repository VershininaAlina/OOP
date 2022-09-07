from audioop import error
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
)
my_set =['123456','password','123456789','12345','2345678','qwerty','234567','111111','1234567890','123123','abc123','1234','password1','iloveyou','1q2w3e4r','000000','qwerty123','zaq12wsx','Dragon1','sunshine','princess','letmein','654321','monkey','27653','1qaz2wsx','123321','qwertyuiop','superman','asdfghjkl']


class Registration:
  def __init__(self, login, password):    
    self.login = login
    self.password = password        
    
  @staticmethod
  def is_include_digit(password):
    for h in password:
      if h in "0123456789":
        return True
    return False
    
  @staticmethod
  def is_include_only_latin(password):
    for i in password:
      if (i not in ascii_letters) and ( i not in digits) :
        return False
    return True  
    
  @staticmethod 
  def is_include_all_register(password):
    Flag = False
    Flag2 = False
    for i1 in password :
      if i1.islower():
        Flag = True
    for i2 in password:
      if i2.isupper():
        Flag2 = True
    if  Flag == True and Flag2 == True:
      return True
    else:
      return False
      
  @staticmethod 
  def check_password_dictionary(password):
    if password.lower() in my_set:
      return True
    else:
      return False
        
  @property
  def login(self):
    return self.__login
    
  @login.setter
  def login(self, login):
    if ("@" not in login) or (login.count("@") != 1):  
      raise ValueError("Логин должен содержать один символ '@'")            
    if '.' in login:
      if login.index('@') > login.index('.'):
        raise ValueError("Логин должен содержать символ '.'")
    else :
      raise ValueError("Login must include at least one ' @ '")        
    self.__login = login

  @property
  def password(self):
    return self.__password 
    
  @password.setter
  def password(self, password):
    if not isinstance(password, str):
      raise TypeError("Пароль должен быть строкой")
    if (len(password) < 5) and (len(password) > 11):
      raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
    if  Registration.is_include_digit(password) == False : 
      raise ValueError('Пароль должен содержать хотя бы одну цифру')
         
    if  Registration.is_include_all_register(password) == False :
      raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')            
    if Registration.is_include_only_latin(password)  == False:
      raise ValueError('Пароль должен содержать только латинский алфавит')
            
    if Registration.check_password_dictionary(password) == True:
      raise ValueError('Ваш пароль содержится в списке самых легких')
            
    self.__password = password     