'''

  ___INTERFACE_______________________________________________________________
    ______________________
        FOMRA 1
        if not self.game.is_finished(s):
            if self.game.is_stuck(s):
                print("stuck")
                return

            move = self.game.get_random_move(s)
            s = self.game.play_move(move[0], move[1], move[2], move[3], s)
            print(s)
            self.update_state(s)
            self.update()
            self.game.change_turn()

            # Schedule the next move after a delay (in milliseconds) -> WTF IS THIS?
            self.root.after(1000, lambda: self.play_random_move(s))

        else:
            print(self.game.winner(s))
            self.root.destroy()
        _______________________    
        FORMA 2
        self.update_state(s)
        self.update()
        self.root.update_idletasks() 
        time.sleep(3) 
        
        while not self.game.is_finished(s):
            if self.game.is_stuck(s):
                print("Stuck")
                break
            
            move = self.game.get_random_move(s)
            s = self.game.play_move(move[0], move[1], move[2], move[3], s)
            print(s)
            self.update_state(s)
            self.update()
            self.game.change_turn()
    
            # Wait for a short time to make the updates visible
            self.root.update_idletasks()            # Update "tasks to do" ???wtf
            time.sleep(1)  # Adjust the delay as needed

        print(self.game.winner(s))
        self.root.destroy()
'''





'''
 def is_threefold_repetition_rule(self):
        #tem que ser por exausatão pois o padrão é especifico
        if len(self.last_nine)==9:
            first = np.array_equal(self.last_nine[0], self.last_nine[4]) and np.array_equal(self.last_nine[4], self.last_nine[8])

            PRECISO DE CONFIRMAR SE A REGRA É ASSIM
            #second = np.array_equal(self.last_nine[1], self.last_nine[5])
            #third = np.array_equal(self.last_nine[2], self.last_nine[6])
            return first #and second and third
        return False    #se for menor que 9, não pode haver repetição
'''




'''

move_0=(0,0,0,2)
move_1= (5,0,5,2)
move_2= (0,2,0,0)
move_3= (5,2,5,0)

move_4= (0,0,0,2)
move_5= (5,0,5,2)
move_6= (0,2,0,0)
move_7= (5,2,5,0)

move_8= (0,0,0,2)
move_9= (5,0,5,2)
move_10= (0,2,0,0)
move_11= (5,2,5,0)

game = Ataxx(6)
s = game.make_s0()
print(s)
count=0

print("count: ", count)
print(game.get_player_turn())
s = game.play_move(move_0[0], move_0[1], move_0[2], move_0[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_1[0], move_1[1], move_1[2], move_1[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_2[0], move_2[1], move_2[2], move_2[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_3[0], move_3[1], move_3[2], move_3[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_4[0], move_4[1], move_4[2], move_4[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_5[0], move_5[1], move_5[2], move_5[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_6[0], move_6[1], move_6[2], move_6[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_7[0], move_7[1], move_7[2], move_7[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_8[0], move_8[1], move_8[2], move_8[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_9[0], move_9[1], move_9[2], move_9[3],s)
print(s)
game.change_turn()
time.sleep(1)

count+=1
print("count: ", count)
print("check: ", game.is_finished(s))
print(game.get_player_turn())
s = game.play_move(move_10[0], move_10[1], move_10[2], move_10[3],s)
print(s)
game.change_turn()
time.sleep(1)

'''

    
