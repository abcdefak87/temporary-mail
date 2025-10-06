#!/usr/bin/env python3
"""
Git Branch & Commit Manager
Automated git operations with remote branch support
"""

import subprocess
import sys
import os
from datetime import datetime

class GitManager:
    def __init__(self):
        self.current_branch = None
        self.remote_branches = []
        self.local_branches = []
        
    def run_git_command(self, command):
        """Execute git command and return output"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True,
                cwd=os.getcwd()
            )
            return result.stdout.strip(), result.returncode
        except Exception as e:
            print(f"❌ Error running command: {e}")
            return "", 1
    
    def check_git_status(self):
        """Check if git repo exists and get status"""
        output, code = self.run_git_command("git status --porcelain")
        if code != 0:
            print("❌ Not a git repository. Initialize first with: git init")
            return False
        
        # Get current branch
        branch_output, _ = self.run_git_command("git branch --show-current")
        self.current_branch = branch_output
        
        # Get all branches
        local, _ = self.run_git_command("git branch")
        self.local_branches = [b.strip().replace('* ', '') for b in local.split('\n') if b]
        
        remote, _ = self.run_git_command("git branch -r")
        self.remote_branches = [b.strip() for b in remote.split('\n') if b]
        
        return True
    
    def display_menu(self):
        """Show interactive menu"""
        print("\n" + "="*50)
        print("🚀 GIT BRANCH & COMMIT MANAGER")
        print("="*50)
        print(f"📍 Current Branch: {self.current_branch}")
        print(f"📁 Repository: {os.path.basename(os.getcwd())}")
        print("\n📋 Options:")
        print("1. Quick commit & push to current branch")
        print("2. Create new branch and switch")
        print("3. Switch to existing branch")
        print("4. Commit to new branch (create + commit + push)")
        print("5. View all branches")
        print("6. Pull latest from remote")
        print("7. Merge branch")
        print("8. Delete branch")
        print("9. Setup remote (if not exists)")
        print("0. Exit")
        print("-"*50)
        
    def quick_commit(self):
        """Quick commit and push to current branch"""
        print(f"\n🔄 Committing to branch: {self.current_branch}")
        
        # Check for changes
        status, _ = self.run_git_command("git status --porcelain")
        if not status:
            print("✅ No changes to commit")
            return
        
        # Show changes
        print("\n📝 Changes to commit:")
        os.system("git status -s")
        
        # Get commit message
        message = input("\n💬 Commit message (or press Enter for auto): ").strip()
        if not message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"Update: {timestamp}"
        
        # Add all changes
        print("\n⏳ Adding all changes...")
        self.run_git_command("git add .")
        
        # Commit
        print(f"⏳ Committing with message: {message}")
        output, code = self.run_git_command(f'git commit -m "{message}"')
        if code == 0:
            print("✅ Commit successful")
        else:
            print(f"❌ Commit failed: {output}")
            return
        
        # Push to remote
        print(f"\n⏳ Pushing to remote branch: origin/{self.current_branch}")
        output, code = self.run_git_command(f"git push origin {self.current_branch}")
        if code == 0:
            print("✅ Push successful!")
        else:
            # Try to set upstream if first push
            print("⏳ Setting upstream and pushing...")
            output, code = self.run_git_command(f"git push -u origin {self.current_branch}")
            if code == 0:
                print("✅ Push successful with upstream set!")
            else:
                print(f"❌ Push failed: {output}")
    
    def create_branch(self, switch=True):
        """Create new branch"""
        branch_name = input("\n🌿 Enter new branch name: ").strip()
        if not branch_name:
            print("❌ Branch name cannot be empty")
            return None
        
        # Check if branch exists
        if branch_name in self.local_branches:
            print(f"⚠️ Branch '{branch_name}' already exists locally")
            return branch_name
        
        # Create branch
        print(f"\n⏳ Creating branch: {branch_name}")
        output, code = self.run_git_command(f"git branch {branch_name}")
        if code == 0:
            print(f"✅ Branch '{branch_name}' created")
            if switch:
                self.switch_branch(branch_name)
            return branch_name
        else:
            print(f"❌ Failed to create branch: {output}")
            return None
    
    def switch_branch(self, branch_name=None):
        """Switch to different branch"""
        if not branch_name:
            print("\n📋 Available branches:")
            for i, branch in enumerate(self.local_branches, 1):
                marker = "→" if branch == self.current_branch else " "
                print(f"{marker} {i}. {branch}")
            
            choice = input("\n🔢 Select branch number (or 0 to cancel): ").strip()
            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(self.local_branches):
                    print("❌ Invalid selection")
                    return
                branch_name = self.local_branches[idx]
            except:
                print("❌ Invalid input")
                return
        
        print(f"\n⏳ Switching to branch: {branch_name}")
        output, code = self.run_git_command(f"git checkout {branch_name}")
        if code == 0:
            self.current_branch = branch_name
            print(f"✅ Switched to branch: {branch_name}")
        else:
            print(f"❌ Failed to switch: {output}")
    
    def commit_new_branch(self):
        """Create new branch, commit, and push"""
        branch = self.create_branch(switch=True)
        if branch:
            self.quick_commit()
    
    def view_branches(self):
        """Display all branches"""
        print("\n🌳 BRANCHES:")
        print("\n📍 Local branches:")
        for branch in self.local_branches:
            marker = "→" if branch == self.current_branch else " "
            print(f"{marker} {branch}")
        
        if self.remote_branches:
            print("\n☁️ Remote branches:")
            for branch in self.remote_branches:
                print(f"  {branch}")
    
    def pull_latest(self):
        """Pull latest from remote"""
        print(f"\n⏳ Pulling latest from origin/{self.current_branch}...")
        output, code = self.run_git_command(f"git pull origin {self.current_branch}")
        if code == 0:
            print("✅ Pull successful")
        else:
            print(f"❌ Pull failed: {output}")
    
    def merge_branch(self):
        """Merge another branch into current"""
        print(f"\n📍 Current branch: {self.current_branch}")
        print("📋 Available branches to merge:")
        
        other_branches = [b for b in self.local_branches if b != self.current_branch]
        for i, branch in enumerate(other_branches, 1):
            print(f"  {i}. {branch}")
        
        choice = input("\n🔢 Select branch to merge (or 0 to cancel): ").strip()
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(other_branches):
                print("❌ Invalid selection")
                return
            source_branch = other_branches[idx]
        except:
            print("❌ Invalid input")
            return
        
        confirm = input(f"\n⚠️ Merge '{source_branch}' into '{self.current_branch}'? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Merge cancelled")
            return
        
        print(f"\n⏳ Merging {source_branch} into {self.current_branch}...")
        output, code = self.run_git_command(f"git merge {source_branch}")
        if code == 0:
            print("✅ Merge successful")
        else:
            print(f"❌ Merge failed: {output}")
    
    def delete_branch(self):
        """Delete a branch"""
        print("\n📋 Branches (excluding current):")
        other_branches = [b for b in self.local_branches if b != self.current_branch]
        
        for i, branch in enumerate(other_branches, 1):
            print(f"  {i}. {branch}")
        
        choice = input("\n🔢 Select branch to delete (or 0 to cancel): ").strip()
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(other_branches):
                print("❌ Invalid selection")
                return
            branch_to_delete = other_branches[idx]
        except:
            print("❌ Invalid input")
            return
        
        confirm = input(f"\n⚠️ Delete branch '{branch_to_delete}'? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Deletion cancelled")
            return
        
        # Delete local branch
        print(f"\n⏳ Deleting local branch: {branch_to_delete}")
        output, code = self.run_git_command(f"git branch -D {branch_to_delete}")
        if code == 0:
            print("✅ Local branch deleted")
        
        # Ask to delete remote
        delete_remote = input("\n🌐 Also delete from remote? (y/n): ")
        if delete_remote.lower() == 'y':
            print(f"⏳ Deleting remote branch...")
            output, code = self.run_git_command(f"git push origin --delete {branch_to_delete}")
            if code == 0:
                print("✅ Remote branch deleted")
            else:
                print(f"⚠️ Could not delete remote: {output}")
    
    def setup_remote(self):
        """Setup or change remote repository"""
        # Check current remote
        remotes, _ = self.run_git_command("git remote -v")
        if remotes:
            print("\n📍 Current remotes:")
            print(remotes)
            change = input("\n🔄 Change remote URL? (y/n): ")
            if change.lower() != 'y':
                return
        
        url = input("\n🔗 Enter GitHub repository URL: ").strip()
        if not url:
            print("❌ URL cannot be empty")
            return
        
        if remotes:
            print("\n⏳ Updating remote origin...")
            self.run_git_command("git remote remove origin")
        else:
            print("\n⏳ Adding remote origin...")
        
        output, code = self.run_git_command(f"git remote add origin {url}")
        if code == 0:
            print("✅ Remote setup successful")
        else:
            print(f"❌ Failed to setup remote: {output}")
    
    def run(self):
        """Main execution loop"""
        if not self.check_git_status():
            return
        
        while True:
            self.display_menu()
            choice = input("\n👉 Your choice: ").strip()
            
            if choice == '1':
                self.quick_commit()
            elif choice == '2':
                self.create_branch()
            elif choice == '3':
                self.switch_branch()
            elif choice == '4':
                self.commit_new_branch()
            elif choice == '5':
                self.view_branches()
            elif choice == '6':
                self.pull_latest()
            elif choice == '7':
                self.merge_branch()
            elif choice == '8':
                self.delete_branch()
            elif choice == '9':
                self.setup_remote()
            elif choice == '0':
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice")
            
            # Refresh status
            self.check_git_status()
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = GitManager()
    manager.run()
