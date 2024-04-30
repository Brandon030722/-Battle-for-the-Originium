import random
import time
import tkinter as tk
import pickle
import sys
import os
from tkinter import messagebox, simpledialog



Cost=1
Card_limited=5
Base1_hp=20
Base2_hp=20
player_hand=[]
player2_hand=[]
deployment_cost = 10
deployment_cost2 = 10




#字典部分
faction_cards = {
    1: {  # 罗德岛分支
        1: ("Amiya", 2, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Amiya.png"),
        2: ("Kal'tsit", 3, 2, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Kal'tsit.png"),
        3: ("Warfarin", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Warfarin.png"),
        4: ("Mudrock", 2, 1, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Mudrock.png"),
        5: ("Eyjafjalla", 3, 1, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Eyjafjalla.png"),
        6: ("Blaze", 2, 1, 5, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Blaze.png"),
        7: ("W", 3, 2, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\W.png"),
        8: ("Kroos", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Luodedao\\Kroos.png")
    },
    2: {  # 卡西米尔分支
        1: ("Nearl", 3, 3, 1, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Nearl.png"),
        2: ("Blemishine", 3, 1, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Blemishine.png"),
        3: ("Mlynar", 4, 1, 1, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Mlynar.png"),
        4: ("Gravel", 1, 1, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Gravel.png"),
        5: ("Flametail", 2, 2, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Flametail.png"),
        6: ("Whislash", 1, 2, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Whislash.png"),
        7: ("Fartooth", 2, 3, 1, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Fartooth.png"),
        8: ("Platinum", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Kaximier\\Platinum.png")
    },
    3: {  # 大炎分支
        1: ("Ch'en", 3, 2, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\chen.png"),
        2: ("Hoshiguma", 1, 1, 5, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\Hoshiguma.png"),
        3: ("Swire", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\Swire.png"),
        4: ("Shu", 3, 1, 7, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\shu.png"),
        5: ("Nian", 2, 2, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\nian.png"),
        6: ("Ling", 2, 1, 1, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\ling.png"),
        7: ("Chongyue", 3, 3, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\chongyue.png"),
        8: ("Dusk", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Dayan\\Dusk.png")
    },
    4: {  # Deep Sea Faction
        1: ("Skadi", 1, 1, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Skadi.png"),
        2: ("Specter", 3, 3, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Specter.png"),
        3: ("Gladiia", 3, 1, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Gladiia.png"),
        4: ("Deepcolor", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Deepcolor.png"),
        5: ("Andreana", 1, 1, 1, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Andreana.png"),
        6: ("Highmore", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Highmore.png"),
        7: ("Thorns", 2, 2, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\Thorns.png"),
        8: ("irene", 3, 2, 5, "D:\\battle_for_the_originium\\Battle for the originium\\Shenhailieren\\irene.png")
    },

    5: {  # Laterno Faction
        1: ("Mostima", 5, 4, 6, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Mostima.png"),
        2: ("Executor", 2, 2, 4, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Executor.png"),
        3: ("Fiammetta", 2, 2, 6, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Fiammetta.png"),
        4: ("Executor", 3, 3, 5, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Executor.png"),
        5: ("Virtuosa", 3, 2, 6, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Virtuosa.png"),
        6: ("Archetto", 1, 1, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Archetto.png"),
        7: ("Spuria", 2, 1, 3, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\Spuria.png"),
        8: ("insider", 1, 2, 2, "D:\\battle_for_the_originium\\Battle for the originium\\Latelan\\insider.png")
    }
}

def loading_screen(duration):
    messagebox.showinfo("Now switch to Another player's turn.switching......\n"
          "************************************************")
    time.sleep(duration)
    messagebox.showinfo("switching completed!")

def draw_card():
    # 随机选择一个阵营
    faction = random.choice(list(faction_cards.keys()))
    # 随机选择该阵营的一张卡牌
    card_number = random.choice(list(faction_cards[faction].keys()))
    # 返回卡牌信息
    return (faction, card_number)
    drawn_card = draw_card()
    drawn_card_info = faction_cards[drawn_card[0]][drawn_card[1]]
    messagebox.showinfo(f"Drawn card: {drawn_card}")
    messagebox.showinfo(f"Card info: Name: {drawn_card_info[0]}, Cost: {drawn_card_info[1]}, Attack: {drawn_card_info[2]}, Health: {drawn_card_info[3]}")

def draw_basic_card():

    return ("Ordinary Operator", 1, 1, 1)  # 名称、费用、攻击力、生命值


def display_card_info(card_info):
    # Display card info without the image path
    return f"Name: {card_info[0]}, Cost: {card_info[1]}, Attack: {card_info[2]}, Health: {card_info[3]}"

##############################################################################################################
#先手玩家的函数


def player_choose_card():
    choice = simpledialog.askstring("Input", "Player A, do you want to draw a (1) Special Card or a (2) Basic Card? Enter 1 or 2:")
    if choice == '1':
        # 抽取特殊卡牌
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        messagebox.showinfo("Drawn Card", f"Drawn Special Card:\nName:\n {card_info[0]}\nCost:\n{card_info[1]}\nAttack:\n{card_info[2]},\nHealth:\n{card_info[3]}")
        player_hand.append(card_info)
    elif choice == '2':
        # 抽取基础卡牌
        card_info = draw_basic_card()
        messagebox.showinfo("Drawn Card", f"Drawn Basic Card:\nName:\n {card_info[0]}\nCost:\n{card_info[1]}\nAttack:\n{card_info[2]},\nHealth:\n{card_info[3]}")
        player_hand.append(card_info)
    else:
        messagebox.showerror("Invalid Input", "Invalid input. Please enter 1 or 2.")
    return player_hand


def initialize_and_modify_hand():


    # 连续抽取五张卡牌，并将每张卡牌添加到玩家的手牌列表中
    for _ in range(5):
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        player_hand.append(card_info)




def display_card_info(card_info):
    # Display card info without the image path
    return f"Name: {card_info[0]}, Cost: {card_info[1]}, Attack: {card_info[2]}, Health: {card_info[3]}"

def remove_two_cards(player_hand):
    if not player_hand:
        messagebox.showinfo("Remove Cards", "No cards in hand to remove.")
        return

    # Creating a string to show the cards in the hand without the image paths
    cards_str = "\n".join(f"{i + 1}: {display_card_info(card)}" for i, card in enumerate(player_hand))
    choices = simpledialog.askstring("Remove Cards", f"Your current hand:\n{cards_str}\nEnter the numbers of the two cards you want to remove (separated by a space):")
    if not choices:
        messagebox.showwarning("Warning", "No input received!")
        return

    try:
        # Convert input string to indices and sort them in reverse order to remove from the list
        indices = sorted([int(choice) - 1 for choice in choices.split()], reverse=True)
        if all(0 <= index < len(player_hand) for index in indices):
            removed_cards_info = []
            for index in indices:
                removed_card = player_hand.pop(index)
                removed_cards_info.append(display_card_info(removed_card))
            # Update the display of the hand after removing the cards
            cards_str = "\n".join(f"{i + 1}: {display_card_info(card)}" for i, card in enumerate(player_hand))
            messagebox.showinfo("Cards Removed", f"Removed cards:\n{'\n'.join(removed_cards_info)}\nThe hand is now:\n{cards_str}")
        else:
            messagebox.showerror("Error", "Invalid card numbers provided.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


def decrease_deployment_cost(amount):
    global deployment_cost  # 指明我们要修改的是全局变量
    if deployment_cost >= amount:
        deployment_cost -= amount
        messagebox.showinfo("Deployment Cost", f"Current deployment cost after decrease: {deployment_cost}")
    else:
        messagebox.showerror("Deployment Cost", "Not enough cost available.")
    return deployment_cost  # 返回更新后的值


def increase_deployment_cost(amount):
    global deployment_cost  # Refer to the global variable
    if (deployment_cost + amount) > 0:  # Check if the new cost is valid
        deployment_cost += amount  # Increase the deployment cost
        # Use messagebox to show the updated cost
        messagebox.showinfo("Deployment Cost Increased", f"Current deployment cost after increase: {deployment_cost}")
    else:
        # Use messagebox to show error if the cost cannot be increased
        messagebox.showerror("Error", "Deployment cost cannot be negative.")
    return deployment_cost  # Return the updated cost


 #######################################################################################################################
#后手玩家的函数

def player2_choose_card():
    global player2_hand  # Using the global variable to store player hand

    # Create a dialog for player to choose type of card to draw
    choice = simpledialog.askstring("Card Choice", "Player B, do you want to draw a (1) Special Card or a (2) Basic Card? Enter 1 or 2:")

    if choice == '1':
        # Draw a special card
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        messagebox.showinfo("Draw Result", f"Drawn Special Card: {card_info[:4]}")  # Do not show card path
        player2_hand.append(card_info)
    elif choice == '2':
        # Draw a basic card
        card_info = draw_basic_card()
        messagebox.showinfo("Draw Result", f"Drawn Basic Card: {card_info[:4]}")  # Show only the relevant card details
        player2_hand.append(card_info)
    else:
        messagebox.showerror("Invalid Input", "Invalid input. Please enter 1 or 2.")

    return player2_hand


def initialize2_and_modify_hand():


    # 连续抽取五张卡牌，并将每张卡牌添加到玩家的手牌列表中
    for _ in range(5):
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        player2_hand.append(card_info)


def remove2_two_cards(player2_hand):
    # Display current hand without showing the image paths
    hand_info = "\n".join([f"{i + 1}: {card[:4]}" for i, card in enumerate(player2_hand)])
    messagebox.showinfo("Current Hand", f"Your current hand:\n{hand_info}")

    # Get input from user
    choices = simpledialog.askstring("Remove Cards",
                                     "Enter the numbers of the two cards you want to remove (separated by a space):")
    if choices:
        indices = sorted([int(choice) - 1 for choice in choices.split()], reverse=True)

        # Check the validity of indices
        if all(0 <= index < len(player2_hand) for index in indices):
            for index in indices:
                removed_card = player2_hand.pop(index)
                messagebox.showinfo("Card Removed", f"Removed card: {removed_card[:4]}")
            hand_info_updated = "\n".join([f"{i + 1}: {card[:4]}" for i, card in enumerate(player2_hand)])
            messagebox.showinfo("Updated Hand", f"The hand is now:\n{hand_info_updated}")
        else:
            messagebox.showerror("Invalid Selection", "One or more selected indices are invalid.")
    else:
        messagebox.showerror("No Input", "No input received.")


def decrease_deployment_cost2(amount):

    global deployment_cost2  # 指明我们要修改的是全局变量
    deployment_cost2 -= amount  # 减少部署费用
    return deployment_cost2  # 返回更新后的值


def increase_deployment_cost2(amount):

    global deployment_cost2  # 指明我们要修改的是全局变量
    deployment_cost2 += amount  # 增加部署费用
    return deployment_cost2  # 返回更新后的值



#########################################################################################################################
#两个玩家的初始函数和行动函数

def main_Begin_A():
    messagebox.showinfo("Welcome", "Welcome to the game! You are the first player. Draw five initial cards and choose three of them.")
    initialize_and_modify_hand()
    remove_two_cards(player_hand)
    player_choose_card()
    current_hand_info = "\n".join([f"{card[:4]}" for card in player_hand])
    messagebox.showinfo("Current Hand", f"Your current hand:\n{current_hand_info}")
    return player_hand

def main_BEGIN_B():
    messagebox.showinfo("Welcome", "Welcome to the game! You are the second player. Draw five initial cards and choose three of them.")
    initialize2_and_modify_hand()
    remove2_two_cards(player2_hand)
    player2_choose_card()
    current_hand_info = "\n".join([f"{card[:4]}" for card in player2_hand])
    messagebox.showinfo("Current Hand", f"Your current hand:\n{current_hand_info}")
    return player2_hand

def main_action_A():
    messagebox.showinfo("Your Turn", "Now it's your turn.")
    player_choose_card()
    current_hand_info = "\n".join([f"{card[:4]}" for card in player_hand])
    messagebox.showinfo("Current Hand", f"Your current hand:\n{current_hand_info}")
    return player_hand

def main_action_B():
    messagebox.showinfo("Your Turn", "Now it's your turn.")
    player2_choose_card()
    current_hand_info = "\n".join([f"{card[:4]}" for card in player2_hand])
    messagebox.showinfo("Current Hand", f"Your current hand:\n{current_hand_info}")
    return player2_hand

#######################################################################################################################
#前端部分
import tkinter as tk
from PIL import Image, ImageTk



class CardGameGUI(tk.Tk):
    def __init__(self, player_number=1):
        super().__init__()
        self.player_number = player_number
        self.title(f"Battle for the Originium - Player {self.player_number}")
        self.geometry("800x700")

        # 根据玩家号分配手牌和部署成本
        if self.player_number == 1:
            self.current_hand = player_hand
            self.deployment_cost = deployment_cost
        else:
            self.current_hand = player2_hand
            self.deployment_cost = deployment_cost2

        # 为每个玩家初始化已部署和敌方卡牌列表
        self.deployed_cards = []
        self.enemy_deployed_cards = []
        self.frontline_cards = []
        self.card_images = []

        self.load_background_images()
        self.setup_game_areas()
        self.add_buttons()
        self.attacked_this_turn = {}  # 追踪每张卡本回合是否已经攻击
        self.attacked_this_turn = set()  # Track cards that have attacked this turn



#######################################################################################################################
#存储和加载游戏状态
    def save_game_state(self):
        game_state = {
            'deployed_cards': self.deployed_cards,
            'enemy_deployed_cards':self.enemy_deployed_cards,
            'frontline_cards': self.frontline_cards
        }
        with open('game_state.pkl', 'wb') as f:
            pickle.dump(game_state, f)
        print("Game state saved.")

    def load_game_state(self):
        try:
            with open('game_state.pkl', 'rb') as f:
                game_state = pickle.load(f)
                self.deployed_cards = game_state['deployed_cards']
                self.frontline_cards = game_state['frontline_cards']
                self.enemy_deployed_cards = game_state['enemy_deployed_cards']
                self.update_ally_deployment()
                self.update_frontline_deployment()
                self.update_enemy_deployment()
                print("Game state loaded.")
        except FileNotFoundError:
            print("No saved game state found.")
            # If no game state is found, do not load anything (start new)


    def load_background_images(self):
        # 加载所有背景图片
        self.enemy_bg_image = ImageTk.PhotoImage(Image.open("D:\\battle_for_the_originium\Background\\1.jpg"))
        self.frontline_bg_image = ImageTk.PhotoImage(Image.open("D:\\battle_for_the_originium\Background\\3.jpg"))
        self.ally_bg_image = ImageTk.PhotoImage(Image.open("D:\\battle_for_the_originium\Background\\2.jpg"))
        self.button_bg_image = ImageTk.PhotoImage(Image.open("D:\\battle_for_the_originium\Background\\1111.jpg"))


#######################################################################################################################
#设置画布与按钮
    def setup_game_areas(self):
        # 创建并设置所有游戏区域
        self.enemy_deployment_frame = self.create_frame_with_background(200, self.enemy_bg_image, tk.TOP)
        self.frontline_frame = self.create_frame_with_background(200, self.frontline_bg_image, tk.TOP)
        self.ally_deployment_frame = self.create_frame_with_background(200, self.ally_bg_image, tk.TOP)


    def add_buttons(self):
        self.button_frame = tk.Frame(self, height=100, bg="white")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)
        button_canvas = tk.Canvas(self.button_frame, height=100)
        button_canvas.pack(fill=tk.BOTH, expand=True)
        button_canvas.create_image(0, 0, image=self.button_bg_image, anchor=tk.NW)

        # 在按钮区域添加操作按钮
        self.deploy_card_button = tk.Button(button_canvas, text="Deploy Card", command=self.deploy_card)
        self.deploy_card_button.pack(side=tk.LEFT, pady=27)

        self.end_turn_button = tk.Button(button_canvas, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack(side=tk.RIGHT, pady=27)

        # 新添加的移动到前线的按钮
        self.move_to_frontline_button = tk.Button(button_canvas, text="Move to Frontline",
                                                  command=self.move_card_to_frontline)
        self.move_to_frontline_button.pack(side=tk.LEFT, padx=10, pady=27)

        self.attack_button = tk.Button(button_canvas, text="Attack", command=self.attack_card)
        self.attack_button.pack(side=tk.LEFT, padx=10, pady=27)

        self.exit_button = tk.Button(button_canvas, text="Exit Game", command=self.exit_game)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=27)

        self.attack_base_button = tk.Button(button_canvas, text="Attack Base", command=self.attack_base)
        self.attack_base_button.pack(side=tk.LEFT, padx=10, pady=27)

        self.display_health_button = tk.Button(button_canvas, text="Display Base Health",command=self.display_base_health)
        self.display_health_button.pack(side=tk.RIGHT, padx=10, pady=27)

    # 你可以在这里继续添加更多按钮


#######################################################################################################################
#游戏开始阶段


    def start_new_game(self):
        # 重置游戏状态，确保从空白开始
        self.deployed_cards = []
        self.frontline_cards = []
        self.update_ally_deployment()
        self.update_frontline_deployment()
        print("New game started.")

    def create_frame_with_background(self, height, bg_image, side):
        frame = tk.Frame(self, height=height)
        frame.pack(fill=tk.X, side=side)
        canvas = tk.Canvas(frame, height=height)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
        return canvas

    def deploy_card(self):
        if not self.current_hand:
            messagebox.showerror("Deploy Card", "No cards to deploy.")
            return

        card_info = "\n".join(
            [f"{index}. {card[0]} (Cost: {card[1]}, Attack: {card[2]}, Health: {card[3]})" for index, card in
             enumerate(self.current_hand, start=1)])
        choice = simpledialog.askinteger("Deploy Card", f"Select a card to deploy by index:\n{card_info}", minvalue=1,
                                         maxvalue=len(self.current_hand))

        if choice is None or choice < 1 or choice > len(self.current_hand):
            messagebox.showerror("Invalid Choice", "Invalid card number entered.")
            return

        choice -= 1  # Adjusting index to be zero-based
        card = self.current_hand.pop(choice)

        if len(card) < 5:
            messagebox.showerror("Error", "Card data is incomplete.")
            return

        name, cost, attack, health, img_path = card
        if self.deployment_cost >= cost:
            self.show_card_on_deployment(img_path, name, cost, attack, health,
                                         self.player_number == 2)  # Adding whether it's an enemy
            self.deployment_cost -= cost
            messagebox.showinfo("Deployed", f"{name} deployed successfully.")
        else:
            messagebox.showerror("Insufficient Cost", "Not enough deployment cost.")

    def display_card(self, card_data, canvas, index):
        # 从路径加载图片
        img = Image.open(card_data['img'])
        img = img.resize((100, 180), Image.Resampling.LANCZOS)  # 调整图片大小
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用以防垃圾回收
        # 计算图像放置位置
        x_position = 10 + 110 * index
        y_position = 10
        # 在画布上创建图像
        image_id = canvas.create_image(x_position, y_position, image=photo_img, anchor=tk.NW)
        # 更新卡牌数据以包含新的 image_id
        card_data['image_id'] = image_id

    def show_card_on_deployment(self, img_path, card_name, cost, attack, health, is_enemy):
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用
        deployment_frame = self.enemy_deployment_frame if is_enemy else self.ally_deployment_frame
        deployed_cards = self.enemy_deployed_cards if is_enemy else self.deployed_cards
        num_cards = len(deployed_cards)
        x_position = 10 + 110 * num_cards
        y_position = 10
        image_id = deployment_frame.create_image(x_position, y_position, image=photo_img, anchor=tk.NW)
        card_data = {
            'img': img_path,
            'image_id': image_id,
            'name': card_name,
            'cost': cost,
            'attack': attack,
            'health': health
        }
        deployed_cards.append(card_data)



    def end_turn(self):
        self.save_game_state()  # Save the game state
        messagebox.showinfo("End Turn", "Ending turn. Switching to next player.")
        self.destroy()
        self.attacked_this_turn.clear()

    def exit_game(self):
        response = messagebox.askyesno("Exit Game", "Are you sure you want to exit the game?")
        if response:
            messagebox.showinfo("Game Over", "You lost the game because you exited early.")
            sys.exit()

    def remove_card_from_ally(self, card_index):
        # 此函数负责从己方部署位中移除选中的卡牌
        if 0 <= card_index < len(self.deployed_cards):
            card_data = self.deployed_cards.pop(card_index)
            # 从画布上删除卡牌的图像
            self.ally_deployment_frame.delete(card_data['image_id'])
            return card_data
        else:
            print("Invalid card index")
            return None

    def deploy_card_to_frontline(self, card_data):
        img_path = card_data['img']
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用防止被回收
        image_id = self.frontline_frame.create_image(10 + 110 * len(self.frontline_cards), 10, image=photo_img,
                                                     anchor=tk.NW)
        card_data['image_id'] = image_id
        card_data['player_number'] = self.player_number  # 添加此行
        self.frontline_cards.append(card_data)




#######################################################################################################################
#更新展示的代码
    def update_ally_deployment(self):
        self.ally_deployment_frame.delete("all")
        self.ally_deployment_frame.create_image(0, 0, image=self.ally_bg_image, anchor=tk.NW)
        for idx, card_data in enumerate(self.deployed_cards):
            self.display_card(card_data, self.ally_deployment_frame, idx)

    def update_frontline_deployment(self):
        # 同理，更新前线显示
        existing_images = {card_data['image_id']: card_data for card_data in self.frontline_cards}
        self.frontline_frame.delete("all")  # 重新绘制背景
        self.frontline_frame.create_image(0, 0, image=self.frontline_bg_image, anchor=tk.NW)

        updated_cards = []
        for idx, card_data in enumerate(self.frontline_cards):
            img_path = card_data['img']
            img = Image.open(img_path)
            img = img.resize((100, 180), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            self.card_images.append(photo_img)
            if card_data['image_id'] in existing_images:
                self.frontline_frame.delete(card_data['image_id'])
            image_id = self.frontline_frame.create_image(10 + 110 * idx, 10, image=photo_img, anchor=tk.NW)
            card_data['image_id'] = image_id
            updated_cards.append(card_data)

        self.frontline_cards = updated_cards

    def update_enemy_deployment(self):
        self.enemy_deployment_frame.delete("all")  # 先清除画布
        self.enemy_deployment_frame.create_image(0, 0, image=self.enemy_bg_image, anchor=tk.NW)  # 重置背景
        # 重新绘制每一张卡牌
        for idx, card_data in enumerate(self.enemy_deployed_cards):
            self.display_card(card_data, self.enemy_deployment_frame, idx)
        print("Enemy cards updated.")


######################################################################################################################
#移动至前线
    def move_card_to_frontline(self):
        cards_to_move = self.deployed_cards if self.player_number == 1 else self.enemy_deployed_cards

        if not cards_to_move:
            messagebox.showinfo("Move to Frontline", "No cards to move.")
            return

        card_options = "\n".join([f"{index}. {card['name']} (Cost: {card['cost']}, Attack: {card['attack']}, Health: {card['health']})"
                                  for index, card in enumerate(cards_to_move, start=1)])
        choice = simpledialog.askinteger("Select Card", f"Select a card to move to the frontline by index:\n{card_options}",
                                         minvalue=1, maxvalue=len(cards_to_move))

        if choice is not None:
            card_index = choice - 1
            card_data = cards_to_move.pop(card_index)
            if self.player_number == 2 and any(c.get('player_number', 1) == 1 for c in self.frontline_cards):
                messagebox.showerror("Move to Frontline", "Cannot move to frontline; enemy cards present.")
                cards_to_move.insert(card_index, card_data)  # Return card to its position if it can't move
            else:
                self.deploy_card_to_frontline(card_data)
                self.update_ally_deployment()  # Update ally deployment area
                self.update_enemy_deployment()  # Update enemy deployment area
                self.update_frontline_deployment()  # Update frontline display
        else:
            messagebox.showerror("Move to Frontline", "Invalid card index or cancelled.")


#######################################################################################################################
#战斗部分

    def initiate_attack(self):
        # Showing attackable cards using a dialog
        options = "\n".join([f"{index}. {card['name']} (Attack: {card['attack']}, Health: {card['health']})"
                             for index, card in enumerate(self.deployed_cards + self.frontline_cards, start=1)])
        choice = simpledialog.askinteger("Select Card to Attack",
                                         f"Select a card to attack with:\n{options}",
                                         minvalue=1, maxvalue=len(self.deployed_cards + self.frontline_cards))

        if choice is not None:
            attacking_card = (self.deployed_cards + self.frontline_cards)[choice - 1]
            self.select_target(attacking_card)
        else:
            messagebox.showerror("Attack Action", "Invalid card index or cancelled.")

    def select_target(self, attacking_card):
        # Choose a target card to attack using a dialog
        target_cards = self.enemy_deployed_cards if attacking_card in self.deployed_cards else self.deployed_cards
        options = "\n".join([f"{index}. {card['name']} (Health: {card['health']})"
                             for index, card in enumerate(target_cards, start=1)])
        choice = simpledialog.askinteger("Select Target",
                                         f"Select a target card to attack:\n{options}",
                                         minvalue=1, maxvalue=len(target_cards))

        if choice is not None:
            target_card = target_cards[choice - 1]
            self.execute_attack(attacking_card, target_card)
        else:
            messagebox.showerror("Attack Target", "Invalid target card index or cancelled.")

    def execute_attack(self, attacking_card, target_card):
        # Execute the attack and update health
        damage = attacking_card['attack']
        target_card['health'] -= damage
        result_message = f"Attacked {target_card['name']} with {attacking_card['name']}, remaining health: {target_card['health']}"
        if target_card['health'] <= 0:
            self.remove_card(target_card)
            result_message += f"\n{target_card['name']} has been destroyed!"
        messagebox.showinfo("Attack Result", result_message)

    def remove_card(self, card_to_remove):
        # Remove card from display and internal data
        frame_to_update = self.enemy_deployment_frame if card_to_remove in self.enemy_deployed_cards else self.ally_deployment_frame
        frame_to_update.delete(card_to_remove['image_id'])
        card_list = self.enemy_deployed_cards if card_to_remove in self.enemy_deployed_cards else self.deployed_cards
        card_list.remove(card_to_remove)
        messagebox.showinfo("Card Removed", f"{card_to_remove['name']} has been removed from the field.")




    def attack_card(self):
        attackable_cards = [card for card in self.deployed_cards + self.frontline_cards if
                            card['player_number'] == self.player_number]

        if not attackable_cards:
            messagebox.showinfo("No Attack", "No cards available to attack.")
            return

        options = "\n".join([f"{idx + 1}. {card['name']} (Attack: {card['attack']}, Health: {card['health']})"
                             for idx, card in enumerate(attackable_cards)])
        card_index = simpledialog.askinteger("Select Card to Attack",
                                             f"Select your card to attack with:\n{options}",
                                             minvalue=1, maxvalue=len(attackable_cards))

        if card_index is None or card_index in self.attacked_this_turn:
            messagebox.showerror("Attack Error", "This card has already attacked this turn or selection cancelled.")
            return

        attacking_card = attackable_cards[card_index - 1]  # Adjust index
        self.attacked_this_turn.add(card_index)  # Mark this card as having attacked

        # Continue with selecting the target and performing the attack...

        # Code to select target follows...
        possible_targets = [card for card in self.enemy_deployed_cards + self.frontline_cards if
                            card['player_number'] != self.player_number]

        if not possible_targets:
            messagebox.showinfo("No Targets", "No targets available.")
            return

        target_options = "\n".join([f"{idx + 1}. {card['name']} (Health: {card['health']})"
                                    for idx, card in enumerate(possible_targets)])
        target_index = simpledialog.askinteger("Select Target to Attack",
                                               f"Select a target to attack:\n{target_options}",
                                               minvalue=1, maxvalue=len(possible_targets))

        if target_index is None:
            return  # User cancelled the action

        target_card = possible_targets[target_index - 1]
        # Execute the attack
        target_card['health'] -= attacking_card['attack']
        if target_card['health'] <= 0:
            self.remove_card(target_card)
            messagebox.showinfo("Attack Result",
                                f"{attacking_card['name']} attacked and destroyed {target_card['name']}.")
        else:
            messagebox.showinfo("Attack Result",
                                f"{attacking_card['name']} attacked {target_card['name']} for {attacking_card['attack']} damage. Remaining health: {target_card['health']}.")

        self.attacked_this_turn.add(attacking_card)
        self.update_ally_deployment()
        self.update_enemy_deployment()
        self.update_frontline_deployment()

    def start_new_turn(self):
        # Reset the set tracking attacks
        self.attacked_this_turn.clear()
        # Message or other turn initialization code
        messagebox.showinfo("New Turn", "A new turn has started.")

    def attack_base(self):
        if self.player_number == 1 and self.frontline_cards and not self.enemy_deployed_cards:
            target_base = 'Base2_hp'
        elif self.player_number == 2 and self.frontline_cards and not self.enemy_deployed_cards:
            target_base = 'Base1_hp'
        else:
            messagebox.showerror("Attack Base", "Cannot attack base. Conditions not met.")
            return

        card_options = "\n".join([f"{index}. {card['name']} (Attack: {card['attack']})"
                                  for index, card in enumerate(self.frontline_cards, start=1)])
        choice = simpledialog.askinteger("Attack Base", f"Select a frontline card to attack the base:\n{card_options}",
                                         minvalue=1, maxvalue=len(self.frontline_cards))

        if choice and (choice - 1 not in self.attacked_this_turn):
            card = self.frontline_cards[choice - 1]
            global Base1_hp, Base2_hp
            damage = card['attack']
            if target_base == 'Base1_hp':
                Base1_hp -= damage
                messagebox.showinfo("Base Attacked", f"Base 1 HP reduced by {damage}. Current HP: {Base1_hp}")
            else:
                Base2_hp -= damage
                messagebox.showinfo("Base Attacked", f"Base 2 HP reduced by {damage}. Current HP: {Base2_hp}")
            self.attacked_this_turn.add(choice - 1)  # Track attack
            if Base1_hp <= 0 or Base2_hp <= 0:
                messagebox.showinfo("Game Over", "A base has been destroyed! \nYou win!\n Game over.")
                self.destroy()
        else:
            messagebox.showerror("Invalid Selection", "Invalid card selection or card has already attacked.")


    def display_base_health(self):
        # Accessing global variables for the health of the bases
        global Base1_hp, Base2_hp
        # Create a message that includes the current health of both bases
        base_health_message = f"Base 1 Health: {Base1_hp}\nBase 2 Health: {Base2_hp}"
        # Display the message in a popup window
        messagebox.showinfo("Base Health", base_health_message)

    def reset_attacks(self):
        # Reset the tracking set at the start of each turn
        self.attacked_this_turn.clear()


#######################################################################################################################
#主函数

if __name__ == '__main__':


    # 玩家1的游戏开始
    main_Begin_A()
    increase_deployment_cost(1)  # 1
    game_gui = CardGameGUI(player_number=1)
    game_gui.mainloop()

    # 玩家2的游戏开始
    main_BEGIN_B()
    increase_deployment_cost2(1)  # 2
    game_gui = CardGameGUI(player_number=2)
    game_gui.load_game_state()
    game_gui.mainloop()

    while Base1_hp > 0 and Base2_hp > 0:
     main_action_A()
     game_gui = CardGameGUI(player_number=1)
     game_gui.load_game_state()
     game_gui.mainloop()

     if Base1_hp <= 0 or Base2_hp <= 0:
         break

     main_action_B()
     game_gui = CardGameGUI(player_number=2)
     game_gui.load_game_state()
     game_gui.mainloop()
     if Base1_hp <= 0 or Base2_hp <= 0:
        break

     print("Game Over")




