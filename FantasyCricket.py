from tkinter import *
from tkinter import messagebox,ttk
from tkinter import simpledialog



def select_player():
    if select.get() == 1:
        avail_point_list.delete(0,END)
        for i in range(len(batsmans)):
            avail_point_list.insert(i,batsmans[i])
    elif select.get() ==2:
        avail_point_list.delete(0, END)
        for i in range(len(bowlers)):
            avail_point_list.insert(i,bowlers[i])
    elif select.get() ==3:
        avail_point_list.delete(0, END)
        for i in range(len(all_rounders)):
            avail_point_list.insert(i,all_rounders[i])
    else:
        avail_point_list.delete(0, END)
        for i in range(len(wicket_keeper)):
            avail_point_list.insert(i,wicket_keeper[i])

def used_point(event):
    global total_player
    global batsman
    global bowler
    global all_round
    global wket_kper
    if total_player < 11:
        player = avail_point_list.get(ANCHOR)
        if player in team:
            messagebox.showwarning('Game says','one player is selected one time')
        else:
            if player in batsmans:
                batsman+=1
                val = check(batsman,bowler,all_round,wket_kper)
                if val:
                    used_point_list.insert(END, player)
                    total_player += 1
                    batsmen_lbl['text'] = 'Batsmen (BAT) : ' + str(batsman)
                    avail_point_lbl['text'] = 'Points Available : ' + str(11 - total_player)
                    used_point_lbl['text'] = 'Points Used : ' + str(total_player)
                    team.append(player)
                else:
                    messagebox.showwarning("Game says", "only 4 batsmans are selected")
                    batsman -=1
            elif player in bowlers:
                bowler +=1
                val = check(batsman, bowler, all_round, wket_kper)
                if val:
                    used_point_list.insert(END, player)
                    total_player += 1
                    bowler_lbl["text"] = 'Bowler (BOW) : '+ str(bowler)
                    avail_point_lbl['text'] = 'Points Available : ' + str(11 - total_player)
                    used_point_lbl['text'] = 'Points Used : ' + str(total_player)
                    team.append(player)
                else:
                    messagebox.showwarning("Game says", "only 4 bowlers are selected")
                    bowler -= 1
            elif player in all_rounders:
                all_round+=1
                val = check(batsman, bowler, all_round, wket_kper)
                if val:
                    used_point_list.insert(END, player)
                    total_player += 1
                    all_rounder_lbl['text'] = 'ALLrounders (AR) : '+str(all_round)
                    avail_point_lbl['text'] = 'Points Available : ' + str(11 - total_player)
                    used_point_lbl['text'] = 'Points Used : ' + str(total_player)
                    team.append(player)
                else:
                    messagebox.showwarning("Game says", "only 4 All Rounders are selected")
                    all_round -= 1
            else:
                wket_kper+=1
                val = check(batsman, bowler, all_round, wket_kper)
                if val:
                    used_point_list.insert(END, player)
                    total_player += 1
                    wicker_kper_lbl['text'] = 'Wicket-keeper (WK) : '+str(wket_kper)
                    avail_point_lbl['text'] = 'Points Available : ' + str(11 - total_player)
                    used_point_lbl['text'] = 'Points Used : '+ str(total_player)
                    team.append(player)
                else:
                    messagebox.showwarning("Game says", "only 1 Wicket Keeper are selected")
                    wket_kper -= 1
    else:
        messagebox.showwarning('Game says','Only 11 players are allowed')

def check(bat,bow,ar,wk):
    if bat <=4 and bow <=4 and ar<=4 and wk <= 1:
        return True
    else:
        return False

def new_team():
    global team_name
    team_name = simpledialog.askstring("Game says ","Enter your Team Name")
    if team_name !='':
        team__lbl['text'] = 'Team Name : '+str(team_name)
        radio_enable()
    else:
        pass

def open_team():
    top = Toplevel(root)
    top.geometry('220x100+450+300')
    top.resizable(0,0)
    top.title('Open Team')
    team_list = ['team 1','team 2','team 3','team 4','team 5','team 5']
    team_select = ttk.Combobox(top,width=20,values=team_list)
    team_select.grid(row=0,column=0,pady=10,padx=45)

    btn = Button(top,text='Open Team',font=('arial',10,'bold'),command=None)
    btn.grid(row=1,column=0,pady=5,padx=20)



def save_team():
    pass


def evaluate_team():
    top = Toplevel(root)
    top.geometry('500x420+330+150')
    top.resizable(0, 0)
    top.title('Evaluate Team')

    Label(top,text='Evaluate The Performance Of Your Fantacy Team',font=('arial',10,'bold')).place(x=80,y=10)

    team_list = ['team 1', 'team 2', 'team 3', 'team 4', 'team 5', 'team 5']
    select_team = ttk.Combobox(top, width=20, values=team_list)
    select_team.set('Select Team')
    select_team.place(x=50,y=50)

    match_list = ['Match 1','Match 2','Match 3','Match 4','Match 5']
    select_match =  ttk.Combobox(top, width=20, values=match_list)
    select_match.set('Select Match')
    select_match.place(x=300,y=50)

    Label(top, text='______________________________________________________________', font=('arial', 10, 'bold')).place(x=30, y=80)
    Label(top, text='Players ', font=('arial', 10, 'bold')).place(x=40, y=110)

    Label(top, text='Points ', font=('arial', 10, 'bold')).place(x=280, y=110)

    player_list = Listbox(top, selectmode=None,font=("times new roman", 10, "bold"),bd=1,fg='blue',relief=RAISED)
    player_list.place(x=40,y=140,height=230,width=200)

    point_list = Listbox(top, selectmode=None,font=("times new roman", 10, "bold"),bd=1,fg='blue',relief=RAISED)
    point_list.place(x=280,y=140,height=230,width=200)

    btn = Button(top, text='Evaluate Scores',width=20, font=('arial', 10, 'bold'), command=None)
    btn.place(x=160,y=380)

def radio_enable():
    bat_radio.config(state='normal')
    bow_radio.config(state='normal')
    ar_radio.config(state='normal')
    wk_radio.config(state='normal')




root = Tk()
root.configure(bg='white')
root.geometry('650x450+250+100')
root.title('Fantasy Cricket ')
root.resizable(0,0)

select = IntVar()
total_player = 0
batsman = 0
bowler =0
all_round= 0
wket_kper = 0
team = []
team_name = ''
batsmans = ['Suresh Raina', 'Shikhar Dhawan', 'Rishan pant', 'Rohit Sharma', 'Virat Kohli']
bowlers = ['Jasprit Bumrah', 'Hardik Pandya', 'Harbhajan Singh', 'Prithvi Shaw','R Ashwin']
all_rounders = ['Krunal Pandya','Bhuvneshwar Kumar','Amit Mishra','Rishi Dhawan']
wicket_keeper = ['M S Dhoni', 'Sayed Kirmani', 'Nayan Mongia', 'Kiran More']

# ................. Creating menubar.....................

main_menu = Menu(root)
root.config(menu=main_menu)

manage_menu = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label='Manage Teams',menu=manage_menu)

#.................. Sub menus...............................

manage_menu.add_command(label='NEW Team',command=new_team)
manage_menu.add_command(label='OPEN Team',command=open_team)
manage_menu.add_command(label='SAVE Team',command=None)
manage_menu.add_command(label='EVALUATE Team',command=evaluate_team)


# .............. frame one ( selection frame ).........................

selection_frame = Frame(root,bd=3,relief=FLAT)
selection_frame.place(x=35,y=40,height=60,width=580)

# .............. Adding widgets in selection frame ..................

Label(selection_frame,text="Your's Selections",font=('arial',10)).grid(row=0,column=0)

batsmen_lbl = Label(selection_frame,text="Batsmen (BAT) ##",font=('arial',10,'bold'))
batsmen_lbl.grid(row=1,column=0,pady=4)
bowler_lbl = Label(selection_frame,text="Bowler (BOW) ##",font=('arial',10,'bold'))
bowler_lbl.grid(row=1,column=1,pady=4,padx=7)
all_rounder_lbl = Label(selection_frame,text="ALLrounders (AR) ##",font=('arial',10,'bold'))
all_rounder_lbl.grid(row=1,column=2,pady=4,padx=7)
wicker_kper_lbl = Label(selection_frame,text="Wicket-keeper (WK) ##",font=('arial',10,'bold'))
wicker_kper_lbl.grid(row=1,column=3,pady=4,padx=7)


# ....................middle GUI part .........................

avail_point_lbl = Label(root,text='Points Available : 11',font=('arial',10,'bold'),bg='white')
avail_point_lbl.place(x=50,y=120)
used_point_lbl = Label(root,text='Points Used : 0',font=('arial',10,'bold'),bg='white')
used_point_lbl.place(x=380,y=120)

#................. Frames  .....................................

avail_point_frame = Frame(root,bd=3,relief='ridge',bg='white')
avail_point_frame.place(x=50,y=150,height=250,width=240)

used_point_frame = Frame(root,bd=3,bg='white',relief='ridge')
used_point_frame.place(x=380,y=150,height=250,width=240)


# ................ avail frame widgets ...................................

# create combobox ..................

bat_radio = Radiobutton(avail_point_frame,text='Bat',variable=select,value=1,bg='white',state='disabled',command=select_player)
bat_radio.place(x=0,y=5)

bow_radio = Radiobutton(avail_point_frame,text='Bow',variable=select,value=2,bg='white',state='disabled',command=select_player)
bow_radio.place(x=50,y=5)

ar_radio = Radiobutton(avail_point_frame,text='Ar',variable=select,value=3,bg='white',state='disabled',command=select_player)
ar_radio.place(x=100,y=5)

wk_radio = Radiobutton(avail_point_frame,text='Wk',variable=select,value=4,bg='white',state='disabled',command=select_player)
wk_radio.place(x=150,y=5)

# creating List box of avail_point_frame ..........................
avail_point_list = Listbox(avail_point_frame, selectmode=SINGLE,font=("times new roman", 10, "bold"),bd=0,fg='blue')
avail_point_list.bind('<<ListboxSelect>>', used_point)
avail_point_list.place(x=0,y=35,height=210,width=232)

# creating List box of used_point_frame and lABEL ..........................
team__lbl = Label(used_point_frame,text="Team Name :",font=('arial',10,'bold'),width=25,bg='white',justify='left',anchor=W)
team__lbl.place(x=0,y=5)
used_point_list = Listbox(used_point_frame, selectmode=SINGLE,font=("times new roman", 10, "bold"),bd=0,fg='blue')
used_point_list.place(x=0,y=35,height=210,width=232)


root.mainloop()