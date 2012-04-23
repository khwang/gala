import command

fleet = command.Fleet(['Foo', 'Bar'])


foo = fleet.getShip('Foo')
bar = fleet.getShip('Bar')

while(True):
   enemyShips = fleet.state.visibleEnemyShips
   target = enemyShips.values()[0]
   position = target['position']
   if (position['x'] == foo.position['x']):
     if (position['y'] < foo.position['y'] and position['y'] >= foo.position['y'] - 3):
        if (foo.facing != 'up'):
          foo.turn('right')
        else:
          foo.shoot()
        fleet.executeOrders()
     elif (position['y'] > foo.position and position['y'] <= foo.position['y'] + 3):
        if (foo.facing != 'down'):
          foo.turn('left')
        else:
          foo.shoot()
        fleet.executeOrders()
     else: 
       if (position['y'] < foo.position['y']):
         if ( foo.facing != 'up' ):
           foo.turn('right')
         else: 
           foo.move(1)
         fleet.executeOrders()   
       else:
         if (foo.facing != 'down' ):
           foo.turn('left')
         else: 
           foo.move(1)
         fleet.executeOrders()
   else: 
      foo.move(1)
      fleet.executeOrders()
    
