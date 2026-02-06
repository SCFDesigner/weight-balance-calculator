import tkinter as tk
from tkinter import ttk
import random
import math
import time
import threading

class AirspeedsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("✈️ Airspeeds Quiz ✈️")
        self.root.geometry("600x900")
        self.root.configure(bg='#2a2a2a')
        self.root.resizable(False, False)
        
        # V-speeds data
        self.vspeeds = {
            'Vr': 65,    # Rotation speed
            'Vx': 73,    # Best angle of climb
            'Vy': 84,    # Best rate of climb
            'Vyse': 84,  # Best rate of climb single engine
            'Vsse': 70,  # Safe single engine speed
            'Vmc': 62,   # Minimum control speed
            'Vcc': 95,   # Cruise climb speed
            'Vs0': 56,   # Stall speed landing config
            'Vs1': 66,   # Stall speed clean config
            'Vne': 167,  # Never exceed speed
            'Vno': 135,  # Normal operating speed
            'Va': 118,   # Maneuvering speed
            'Vo': 118,   # Operating speed
            'Vle': 93,   # Landing gear extended speed
            'Vlo': 93,   # Landing gear operating speed
            'Vfe': 119,  # Flaps extended speed
            'Vapp': 90,  # Approach speed
            'Vfinal': 70 # Final approach speed
        }
        
        # Quiz state
        self.current_index = 0
        self.quiz_order = []
        self.entries = []
        self.labels = []
        self.fireworks_active = False
        
        # Create GUI
        self.create_widgets()
        self.start_new_quiz()
        
    def create_widgets(self):
        """Create the main GUI widgets"""
        # Title
        title_label = tk.Label(self.root, text="✈️ AIRSPEEDS QUIZ ✈️", 
                              font=('Arial', 20, 'bold'), 
                              bg='#2a2a2a', fg='white')
        title_label.pack(pady=(15, 20))
        
        # Instructions
        instructions = tk.Label(self.root, 
                               text="Enter the airspeed for each V-speed and press Enter\nWrong answer resets the quiz!",
                               font=('Arial', 11), 
                               bg='#2a2a2a', fg='white')
        instructions.pack(pady=(0, 15))
        
        # Main quiz frame
        self.quiz_frame = tk.Frame(self.root, bg='#2a2a2a')
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        # Canvas for fireworks
        self.canvas = tk.Canvas(self.root, bg='#2a2a2a', highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.place_forget()  # Hide canvas initially
        
    def create_quiz_entries(self):
        """Create entry fields for the quiz"""
        # Clear existing widgets
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        
        self.entries = []
        self.labels = []
        
        for i, vspeed in enumerate(self.quiz_order):
            # Create frame for each row
            row_frame = tk.Frame(self.quiz_frame, bg='#2a2a2a')
            row_frame.pack(fill=tk.X, pady=2)
            
            # V-speed label
            label = tk.Label(row_frame, text=f"{vspeed}:", 
                           font=('Arial', 14, 'bold'), 
                           bg='#2a2a2a', fg='white', width=8, anchor='e')
            label.pack(side=tk.LEFT, padx=(0, 10))
            self.labels.append(label)
            
            # Entry field
            entry = tk.Entry(row_frame, font=('Arial', 14), width=8, 
                           bg='white', fg='black', justify='center',
                           relief='solid', bd=2)
            entry.pack(side=tk.LEFT, padx=(0, 10))
            entry.bind('<Return>', lambda e, idx=i: self.check_answer(idx))
            entry.bind('<KeyPress>', lambda e, idx=i: self.on_key_press(e, idx))
            self.entries.append(entry)
            
            # Status indicator
            status_label = tk.Label(row_frame, text="", 
                                  font=('Arial', 12, 'bold'), 
                                  bg='#2a2a2a', width=3)
            status_label.pack(side=tk.LEFT, padx=(10, 0))
            
        # Focus on first entry
        if self.entries:
            self.entries[0].focus_set()
            
    def on_key_press(self, event, index):
        """Handle key press events"""
        # Only allow digits and backspace/delete
        if event.char.isdigit() or event.keysym in ['BackSpace', 'Delete']:
            return True
        else:
            return "break"
            
    def check_answer(self, index):
        """Check if the answer is correct"""
        if self.fireworks_active:
            return
            
        entry = self.entries[index]
        vspeed = self.quiz_order[index]
        correct_answer = self.vspeeds[vspeed]
        
        try:
            user_answer = int(entry.get())
        except ValueError:
            self.wrong_answer()
            return
            
        if user_answer == correct_answer:
            # Correct answer
            entry.configure(bg='#90EE90', state='disabled')  # Light green
            status_label = entry.master.winfo_children()[2]
            status_label.configure(text="✓", fg='#90EE90')
            
            # Move to next question
            self.current_index += 1
            if self.current_index < len(self.quiz_order):
                self.entries[self.current_index].focus_set()
            else:
                # All correct - show fireworks!
                self.show_fireworks()
        else:
            # Wrong answer
            self.wrong_answer()
            
    def wrong_answer(self):
        """Handle wrong answer - reset quiz"""
        # Flash red briefly
        for entry in self.entries:
            entry.configure(bg='#FFB6C1')  # Light red
        
        self.root.after(500, self.start_new_quiz)
        
    def start_new_quiz(self):
        """Start a new quiz with shuffled order"""
        self.current_index = 0
        self.quiz_order = list(self.vspeeds.keys())
        random.shuffle(self.quiz_order)
        self.create_quiz_entries()
        
    def show_fireworks(self):
        """Show fireworks animation"""
        self.fireworks_active = True
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Show canvas
        
        # Create multiple fireworks
        fireworks_thread = threading.Thread(target=self.animate_fireworks)
        fireworks_thread.daemon = True
        fireworks_thread.start()
        
    def animate_fireworks(self):
        """Animate fireworks for 10 seconds"""
        start_time = time.time()
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', 
                 '#00FFFF', '#FFA500', '#FF69B4', '#32CD32', '#FFD700']
        
        while time.time() - start_time < 10:
            # Create a firework
            self.create_firework(colors)
            time.sleep(0.3)
            
        # Clear canvas and reset
        self.root.after(0, self.finish_fireworks)
        
    def create_firework(self, colors):
        """Create a single firework"""
        # Random starting position at bottom
        start_x = random.randint(100, 500)
        start_y = 750
        
        # Random explosion position
        explode_x = random.randint(150, 450)
        explode_y = random.randint(200, 400)
        
        color = random.choice(colors)
        
        # Animate rocket going up
        self.animate_rocket(start_x, start_y, explode_x, explode_y, color)
        
    def animate_rocket(self, start_x, start_y, explode_x, explode_y, color):
        """Animate rocket trail and explosion"""
        # Create rocket trail
        steps = 20
        for i in range(steps):
            if not self.fireworks_active:
                return
                
            x = start_x + (explode_x - start_x) * i / steps
            y = start_y + (explode_y - start_y) * i / steps
            
            # Draw rocket
            rocket = self.canvas.create_oval(x-2, y-2, x+2, y+2, 
                                           fill=color, outline=color)
            
            # Schedule cleanup
            self.root.after(50, lambda r=rocket: self.canvas.delete(r))
            time.sleep(0.02)
            
        # Create explosion
        self.root.after(0, lambda: self.create_explosion(explode_x, explode_y, color))
        
    def create_explosion(self, x, y, color):
        """Create explosion effect"""
        if not self.fireworks_active:
            return
            
        particles = []
        num_particles = 20
        
        for i in range(num_particles):
            angle = (2 * math.pi * i) / num_particles
            speed = random.uniform(30, 80)
            
            # Create particle
            particle_x = x
            particle_y = y
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            
            particle = self.canvas.create_oval(particle_x-3, particle_y-3, 
                                             particle_x+3, particle_y+3,
                                             fill=color, outline=color)
            particles.append((particle, dx, dy, particle_x, particle_y))
            
        # Animate particles
        self.animate_particles(particles)
        
    def animate_particles(self, particles):
        """Animate explosion particles"""
        def update_particles(step=0):
            if not self.fireworks_active or step > 30:
                # Clean up particles
                for particle, _, _, _, _ in particles:
                    try:
                        self.canvas.delete(particle)
                    except:
                        pass
                return
                
            for particle, dx, dy, start_x, start_y in particles:
                new_x = start_x + dx * step * 0.1
                new_y = start_y + dy * step * 0.1 + step * step * 0.05  # Gravity
                
                try:
                    self.canvas.coords(particle, new_x-2, new_y-2, new_x+2, new_y+2)
                except:
                    pass
                    
            self.root.after(30, lambda: update_particles(step + 1))
            
        update_particles()
        
    def finish_fireworks(self):
        """Clean up after fireworks"""
        self.canvas.delete("all")
        self.canvas.place_forget()  # Hide canvas
        self.fireworks_active = False
        
        # Show completion message
        completion_label = tk.Label(self.root, 
                                  text="🎉 PERFECT SCORE! 🎉\nPress any key to start again", 
                                  font=('Arial', 20, 'bold'), 
                                  bg='#2a2a2a', fg='#90EE90')
        completion_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Bind key to restart
        self.root.bind('<Key>', lambda e: self.restart_quiz(completion_label))
        self.root.focus_set()
        
    def restart_quiz(self, completion_label):
        """Restart the quiz"""
        completion_label.destroy()
        self.root.unbind('<Key>')
        self.start_new_quiz()

def main():
    root = tk.Tk()
    app = AirspeedsQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
