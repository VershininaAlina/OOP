class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class User:
    def __init__(self, login , balance = 0):
        self.login = login
        self.balance = balance
        
    def __str__(self):
        return (f"Пользователь {self.login}, баланс - {self.balance}")   

    #Метод поможет узнать баланс пользователя
    @property
    def balance(self):
        return self.__balance
      
    #устанавливаем баланс 
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    #метод пополнение баланса  
    def deposit(self, value):  
        self.__balance = self.__balance + value   
   
  #метод оплаты заказа вызываемый в методе order
    def payment (self, pay):
        if  self.__balance < pay:
            print("Не хватает средств на балансе. Пополните счет")
            return False
        else:
          #Пересчитывем баланс пользователя вычитая сумму заказа
            self.__balance =  self.__balance - pay
            return True
        
class Cart:
    def __init__(self, user):
        self.goods = {}
        self.user = user
        self.__total = 0  

    #Метод возвращающий текущую сумму корзины
    @property
    def total(self):
        return self.__total
      
    #Метод добавления товара в корзину в количестве "count_prod"
    def add(self, product, count_prod = 1):
      
      #Если еще нет блюда в Корзине(словаре goods), то создаем новое значение словаря со значение count_prod, по умолчанию 1 
      #Добавляем новое блюдо в количестве укзанном в методе и пересчитываем общую сумму корзины (__total)
      
        if product not in self.goods:
            self.goods[product] = count_prod 
            self.__total +=  product.price * count_prod
          
          #Если блюдо есть, то увеличиваем количество на указанное в методе (count_prod, по умолчанию 1) и пересчитываем общую сумму корзины (__total)
        else:     
            self.goods[product] += count_prod       
            self.__total +=  count_prod   * product.price

  #Метод удаляющий продукт из корзины на количество (count_prod , по умолчанию 1)
          
    def remove(self, product,  count_prod = 1):
      # Пересчитываем итоговую сумму корзины(__total) путем вычитания из суммы корзины количества товара в корзине * цену товара
      
      #Если пользователь пытается удалить больше, чем есть в корзине, то удаляем полностью это блюдо из словаря     
        if self.goods[product] <= count_prod:
            self.__total -= self.goods[product] * product.price
            del self.goods[product]

          #Если количество удаляемое меньше, то пересчитываем сумму корзины(__total)  и вычитаем из количества блюда в корзине  количество count_prod передаваемое в методе
        else:
            self.__total -= count_prod * product.price
            self.goods[product] =  self.goods[product] - count_prod
          
    #    Метод оплаты, который вызывает метод  payment класса User  
    def order(self):
        Flag = User.payment(self.user, self.__total)   
        if Flag == True:
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")  
          
    #Метод печати чека, в котором также реализована сортировка корзины в алфавитном порядке
          
    def print_check(self):
        sort_list = sorted(self.goods.items(), key=lambda x: x[0].name)
        sort_list1 = dict(sort_list)
        print("---Your check---")
        for k, v in sort_list1.items():
            print(f"{k.name} {k.price} {v} {k.price * v}") 
                       
        print(f"---Total: {self.total}---")         
          