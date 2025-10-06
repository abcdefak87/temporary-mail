#!/usr/bin/env python3
"""
Git Visual Commit Manager
Shows branch graph visualization for every commit
"""

import subprocess
import os
import sys
from datetime import datetime

class GitVisualManager:
    def __init__(self):
        self.setup_git_config()
        
    def run_command(self, cmd, capture=True):
        """Run command and return output"""
        if capture:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr, result.returncode
        else:
            return subprocess.run(cmd, shell=True)
    
    def setup_git_config(self):
        """Setup git aliases and configuration for visual display"""
        aliases = [
            ('graph', 'log --graph --pretty=format:"%C(auto)%h%d %C(blue)%ar %C(green)%an%C(reset) %s" --all'),
            ('lg', 'log --color --graph --pretty=format:"%C(auto)%h%d %C(blue)%ar %C(green)%an%C(reset) %s" --abbrev-commit --all'),
            ('tree', 'log --graph --abbrev-commit --decorate --format=format:"%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)" --all'),
            ('visual', 'log --graph --pretty=format:"%C(yellow)%h%C(reset) %C(red)%d%C(reset) %s %C(green)(%cr) %C(blue)<%an>%C(reset)" --abbrev-commit --date=relative --all'),
            ('branches', 'log --graph --pretty=format:"%C(auto)%h%d %s %C(green)(%ar) %C(blue)<%an>%C(reset)" --abbrev-commit --all --branches'),
        ]
        
        print("⚙️ Setting up Git visual aliases...")
        for alias_name, alias_cmd in aliases:
            cmd = f'git config --global alias.{alias_name} "{alias_cmd}"'
            self.run_command(cmd)
        
        # Set commit message template
        template_path = os.path.join(os.getcwd(), '.gitmessage')
        if os.path.exists(template_path):
            self.run_command(f'git config --local commit.template {template_path}')
    
    def show_graph(self, lines=20):
        """Display git graph"""
        print("\n" + "="*80)
        print("📊 GIT BRANCH GRAPH VISUALIZATION")
        print("="*80 + "\n")
        
        cmd = f"git log --graph --pretty=format:'%C(auto)%h%d %C(blue)%ar %C(green)%an%C(reset) %s' --abbrev-commit --all -n {lines}"
        stdout, stderr, code = self.run_command(cmd)
        
        if code == 0:
            print(stdout)
        else:
            print(f"❌ Error: {stderr}")
        
        print("\n" + "="*80)
    
    def commit_with_visual(self):
        """Commit changes and show visual graph"""
        # Check for changes
        stdout, _, _ = self.run_command("git status --porcelain")
        if not stdout:
            print("✅ No changes to commit")
            return
        
        # Show current status
        print("\n📝 Current changes:")
        os.system("git status -s")
        
        # Get commit type
        print("\n📌 Commit Types:")
        types = [
            "1. feat     - New feature",
            "2. fix      - Bug fix", 
            "3. docs     - Documentation",
            "4. style    - Code style",
            "5. refactor - Code refactoring",
            "6. test     - Add tests",
            "7. chore    - Maintenance",
            "8. perf     - Performance",
            "9. ci       - CI/CD changes",
            "10. build   - Build changes"
        ]
        for t in types:
            print(f"   {t}")
        
        choice = input("\n🔢 Select type (1-10): ").strip()
        type_map = {
            '1': 'feat', '2': 'fix', '3': 'docs', '4': 'style',
            '5': 'refactor', '6': 'test', '7': 'chore', '8': 'perf',
            '9': 'ci', '10': 'build'
        }
        
        commit_type = type_map.get(choice, 'chore')
        
        # Get scope (optional)
        scope = input("📦 Scope (optional, press Enter to skip): ").strip()
        
        # Get description
        description = input("📝 Description (imperative, present tense): ").strip()
        if not description:
            description = f"update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Build commit message
        if scope:
            commit_msg = f"{commit_type}({scope}): {description}"
        else:
            commit_msg = f"{commit_type}: {description}"
        
        # Add all changes
        print("\n⏳ Staging changes...")
        self.run_command("git add .")
        
        # Commit
        print(f"⏳ Committing: {commit_msg}")
        stdout, stderr, code = self.run_command(f'git commit -m "{commit_msg}"')
        
        if code == 0:
            print("✅ Commit successful!")
            
            # Show the new graph
            self.show_graph()
            
            # Ask to push
            push = input("\n🚀 Push to remote? (y/n): ")
            if push.lower() == 'y':
                branch, _, _ = self.run_command("git branch --show-current")
                branch = branch.strip()
                print(f"⏳ Pushing to origin/{branch}...")
                stdout, stderr, code = self.run_command(f"git push origin {branch}")
                
                if code != 0:
                    # Try with upstream
                    print("⏳ Setting upstream...")
                    stdout, stderr, code = self.run_command(f"git push -u origin {branch}")
                
                if code == 0:
                    print("✅ Push successful!")
                    # Show graph again with remote
                    self.show_graph()
                else:
                    print(f"❌ Push failed: {stderr}")
        else:
            print(f"❌ Commit failed: {stderr}")
    
    def interactive_menu(self):
        """Interactive menu with visual options"""
        while True:
            print("\n" + "="*60)
            print("🎯 GIT VISUAL COMMIT MANAGER")
            print("="*60)
            
            # Show mini graph (last 5 commits)
            print("\n📊 Recent commits:")
            cmd = "git log --graph --pretty=format:'%C(auto)%h%d %s' --abbrev-commit -n 5"
            stdout, _, _ = self.run_command(cmd)
            print(stdout)
            
            print("\n📋 Options:")
            print("1. 📝 Commit with visualization")
            print("2. 📊 Show full branch graph")
            print("3. 🌳 Show tree view")
            print("4. 🔄 Pull with graph")
            print("5. 🌿 Create branch")
            print("6. 🔀 Switch branch")
            print("7. 📈 Show all branches graph")
            print("8. 📜 Show detailed log")
            print("9. ⚙️  Setup git aliases")
            print("0. 🚪 Exit")
            print("-"*60)
            
            choice = input("\n👉 Your choice: ").strip()
            
            if choice == '1':
                self.commit_with_visual()
            elif choice == '2':
                lines = input("📊 How many commits to show? (default 20): ").strip()
                lines = int(lines) if lines.isdigit() else 20
                self.show_graph(lines)
            elif choice == '3':
                os.system("git tree")
            elif choice == '4':
                branch, _, _ = self.run_command("git branch --show-current")
                print(f"⏳ Pulling origin/{branch.strip()}...")
                os.system(f"git pull origin {branch.strip()}")
                self.show_graph(10)
            elif choice == '5':
                name = input("🌿 Branch name: ").strip()
                if name:
                    os.system(f"git checkout -b {name}")
                    self.show_graph(10)
            elif choice == '6':
                print("\n📋 Available branches:")
                os.system("git branch -a")
                name = input("\n🔄 Switch to branch: ").strip()
                if name:
                    os.system(f"git checkout {name}")
                    self.show_graph(10)
            elif choice == '7':
                os.system("git branches")
            elif choice == '8':
                os.system("git lg")
            elif choice == '9':
                self.setup_git_config()
                print("✅ Git aliases configured!")
            elif choice == '0':
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice")
            
            if choice != '0':
                input("\nPress Enter to continue...")

def main():
    manager = GitVisualManager()
    
    # If arguments provided, use them
    if len(sys.argv) > 1:
        if sys.argv[1] == 'commit':
            manager.commit_with_visual()
        elif sys.argv[1] == 'graph':
            manager.show_graph()
        elif sys.argv[1] == 'setup':
            manager.setup_git_config()
            print("✅ Git visual configuration complete!")
        else:
            manager.interactive_menu()
    else:
        manager.interactive_menu()

if __name__ == "__main__":
    main()
