#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Account:
  def __init__(self,accountnunber,balance):
    self.__AccountNumber = accountnunber
    self.__Balance = balance

  def GetAccountNumber(self):
    return self.__AccountNumber

  def GetBalance(self):
    return self.__Balance

  def SetAccountNumber(self, no):
    self.__AccountNumber = no

  def SetBalance(self, bal):
    self.__Balance = bal

  class SavingsAccount(Account):
    def _init_(self,AccountNumber,Balance, paymentinterval, regularamount):
      super().__init__(AccountNumber,Balance)
      self.__paymentinterval = paymentinterval
      self.__regularamount = regularamount




