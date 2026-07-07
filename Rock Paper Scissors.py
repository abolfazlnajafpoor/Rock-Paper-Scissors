import random
import time
import os

class RockPaperScissors:
    def __init__(self):
        self.choices = ["سنگ", "کاغذ", "قیچی"]
        self.emoji = {"سنگ": "🪨", "کاغذ": "📄", "قیچی": "✂️"}
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 5
        self.history = []
        self.difficulty = "متوسط"
        self.colors = {
            "green": "\033[92m",
            "red": "\033[91m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "purple": "\033[95m",
            "reset": "\033[0m"
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_colored(self, text, color="reset"):
        print(f"{self.colors.get(color, self.colors['reset'])}{text}{self.colors['reset']}")
    
    def show_menu(self):
        self.clear_screen()
        print("=" * 50)
        self.print_colored("🎮 بازی سنگ، کاغذ، قیچی - نسخه حرفه‌ای", "purple")
        print("=" * 50)
        print(f"📊 امتیاز شما: {self.player_score} | کامپیوتر: {self.computer_score}")
        print(f"🏆 دور: {self.rounds_played}/{self.max_rounds}")
        print(f"⚙️ سطح دشواری: {self.difficulty}")
        print(f"📜 تاریخچه: {len(self.history)} حرکت ثبت شده")
        print("-" * 50)
        print("1️⃣  شروع بازی جدید")
        print("2️⃣  تنظیم سطح دشواری")
        print("3️⃣  نمایش تاریخچه")
        print("4️⃣  تنظیم تعداد دورها (فعلاً ۵ دور)")
        print("5️⃣  خروج از بازی")
        print("-" * 50)
    
    def set_difficulty(self):
        self.clear_screen()
        print("سطح دشواری را انتخاب کنید:")
        print("1. آسان (کامپیوتر گاهی اشتباه می‌کند)")
        print("2. متوسط (کامپیوتر هوشمندانه بازی می‌کند)")
        print("3. سخت (کامپیوتر همیشه بهترین انتخاب را دارد)")
        
        choice = input("انتخاب شما (۱-۳): ")
        if choice == "1":
            self.difficulty = "آسان"
        elif choice == "2":
            self.difficulty = "متوسط"
        elif choice == "3":
            self.difficulty = "سخت"
        else:
            print("انتخاب نامعتبر! سطح متوسط انتخاب شد.")
            self.difficulty = "متوسط"
        
        self.print_colored(f"✅ سطح دشواری به {self.difficulty} تغییر یافت!", "green")
        time.sleep(1.5)
    
    def computer_choice_strategy(self):
        if self.difficulty == "آسان":
            if random.random() < 0.3:
                return random.choice(self.choices)
            else:
                return self.smart_choice()
        elif self.difficulty == "سخت":
            return self.smart_choice()
        else:
            if random.random() < 0.5:
                return self.smart_choice()
            else:
                return random.choice(self.choices)
    
    def smart_choice(self):
        if not self.history:
            return random.choice(self.choices)
        
        last_player_move = self.history[-1]["player"]
        
        if last_player_move == "سنگ":
            return "کاغذ"
        elif last_player_move == "کاغذ":
            return "قیچی"
        elif last_player_move == "قیچی":
            return "سنگ"
        
        return random.choice(self.choices)
    
    def simulate_computer_choice(self):
        print("\n🤖 کامپیوتر در حال انتخاب...", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        time.sleep(0.3)
        print()
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "مساوی", f"هر دو {self.emoji[player]} انتخاب کردید!"
        
        win_conditions = {
            "سنگ": "قیچی",
            "کاغذ": "سنگ",
            "قیچی": "کاغذ"
        }
        
        if win_conditions[player] == computer:
            return "player", f"{self.emoji[player]} {player} بر {self.emoji[computer]} {computer} غلبه کرد!"
        else:
            return "computer", f"{self.emoji[computer]} {computer} بر {self.emoji[player]} {player} غلبه کرد!"
    
    def play_round(self):
        self.clear_screen()
        print(f"🎯 دور {self.rounds_played + 1} از {self.max_rounds}")
        print("=" * 40)
        
        print("انتخاب خود را بکنید:")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {self.emoji[choice]} {choice}")
        
        player_input = input("\nعدد یا نام انتخاب را وارد کنید: ").strip()
        
        if player_input in ["1", "2", "3"]:
            player_choice = self.choices[int(player_input) - 1]
        elif player_input in self.choices:
            player_choice = player_input
        else:
            self.print_colored("❌ ورودی نامعتبر است! لطفاً دوباره تلاش کنید.", "red")
            time.sleep(1.5)
            return self.play_round()
        
        self.simulate_computer_choice()
        computer_choice = self.computer_choice_strategy()
        
        print(f"\n👤 شما: {self.emoji[player_choice]} {player_choice}")
        print(f"🤖 کامپیوتر: {self.emoji[computer_choice]} {computer_choice}")
        
        result, description = self.determine_winner(player_choice, computer_choice)
        
        self.history.append({
            "round": self.rounds_played + 1,
            "player": player_choice,
            "computer": computer_choice,
            "result": result
        })
        
        print("-" * 40)
        if result == "player":
            self.player_score += 1
            self.print_colored(f"✅ {description}", "green")
            self.print_colored("🎉 شما برنده این دور شدید!", "green")
        elif result == "computer":
            self.computer_score += 1
            self.print_colored(f"❌ {description}", "red")
            self.print_colored("😔 کامپیوتر برنده این دور شد!", "red")
        else:
            self.print_colored(f"⚖️ {description}", "yellow")
            self.print_colored("🤝 این دور مساوی شد!", "yellow")
        
        self.rounds_played += 1
        time.sleep(2)
    
    def show_history(self):
        self.clear_screen()
        print("📜 تاریخچه بازی:")
        print("=" * 50)
        
        if not self.history:
            print("هنوز هیچ بازی انجام نداده‌اید!")
        else:
            for record in self.history[-5:]:
                emoji_player = self.emoji[record["player"]]
                emoji_computer = self.emoji[record["computer"]]
                result_emoji = "🎉" if record["result"] == "player" else "💻" if record["result"] == "computer" else "🤝"
                print(f"دور {record['round']}: {result_emoji} شما {emoji_player} vs {emoji_computer} کامپیوتر")
        
        print("=" * 50)
        input("\nبرای ادامه Enter بزنید...")
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.history = []
        self.print_colored("🔄 بازی ریست شد!", "blue")
        time.sleep(1)
    
    def play(self):
        while True:
            self.show_menu()
            
            choice = input("\nانتخاب کنید (۱-۵): ")
            
            if choice == "1":
                self.reset_game()
                while self.rounds_played < self.max_rounds:
                    self.play_round()
                
                self.clear_screen()
                print("🏆 نتیجه نهایی:")
                print("=" * 40)
                print(f"👤 شما: {self.player_score} امتیاز")
                print(f"🤖 کامپیوتر: {self.computer_score} امتیاز")
                
                if self.player_score > self.computer_score:
                    self.print_colored("🎊 تبریک! شما برنده بازی شدید!", "green")
                elif self.computer_score > self.player_score:
                    self.print_colored("😔 کامپیوتر برنده بازی شد! دفعه بعد تلاش بیشتری کن!", "red")
                else:
                    self.print_colored("🤝 بازی مساوی شد!", "yellow")
                
                input("\nبرای ادامه Enter بزنید...")
                
            elif choice == "2":
                self.set_difficulty()
                
            elif choice == "3":
                self.show_history()
                
            elif choice == "4":
                self.clear_screen()
                try:
                    new_rounds = int(input("تعداد دورهای جدید را وارد کنید: "))
                    if 1 <= new_rounds <= 10:
                        self.max_rounds = new_rounds
                        self.print_colored(f"✅ تعداد دورها به {new_rounds} تغییر یافت!", "green")
                    else:
                        self.print_colored("❌ تعداد دورها باید بین ۱ تا ۱۰ باشد!", "red")
                except ValueError:
                    self.print_colored("❌ لطفاً یک عدد معتبر وارد کنید!", "red")
                time.sleep(1.5)
                
            elif choice == "5":
                self.clear_screen()
                self.print_colored("👋 خداحافظ! ممنون از بازی کردن.", "purple")
                break
                
            else:
                self.print_colored("❌ انتخاب نامعتبر! لطفاً دوباره تلاش کنید.", "red")
                time.sleep(1.5)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
