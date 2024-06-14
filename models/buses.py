from db import cursor,conn

class Buses:
   
  TABLE_BUSES = "buses" 
  def __init__(self,location):
      self.id = None
      self.location = location
      
  @classmethod
  def create_table(cls):
    sql = f"""
    
        """