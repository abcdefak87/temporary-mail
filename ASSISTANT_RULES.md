# AI Assistant Operating Rules

## 1. Code Development Standards

### 1.1 Code Quality
- **Clean Code**: Write readable, self-documenting code with clear variable names
- **Error Handling**: Implement comprehensive try-catch blocks and validation
- **Comments**: Add explanatory comments for complex logic only
- **DRY Principle**: Don't Repeat Yourself - create reusable functions
- **SOLID Principles**: Follow object-oriented design principles

### 1.2 Language-Specific Rules
- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use ES6+ features, async/await for promises
- **TypeScript**: Leverage type safety, avoid 'any' type
- **HTML/CSS**: Use semantic HTML, BEM methodology for CSS

## 2. Tool Usage Protocol

### 2.1 File Operations
- **Always Read First**: Never edit without reading file contents
- **Verify Existence**: Check if files exist before operations
- **Backup Important Files**: Create .backup copies when necessary
- **Use Appropriate Tools**: 
  - `find_by_name` for locating files
  - `grep_search` for content search
  - `MultiEdit` for multiple changes in same file

### 2.2 Command Execution
- **No CD Commands**: Use cwd parameter instead
- **Safety First**: Never auto-run destructive commands
- **Validate Input**: Check command syntax before execution
- **Monitor Output**: Track long-running processes

## 3. Communication Standards

### 3.1 Response Structure
```markdown
# Clear Heading
Brief explanation of what I'm doing

## Implementation
- **Step 1**: Description
- **Step 2**: Description

## Status
✅ Completed tasks
⏳ In progress
❌ Failed/Issues
```

### 3.2 Code References
- File paths: `path/to/file.py`
- Functions: `functionName()`
- Classes: `ClassName`
- Inline code: `variable_name`

## 4. Security Protocols

### 4.1 Sensitive Information
- **Never Hardcode**: API keys, passwords, tokens
- **Use Config Files**: Store secrets in .env or config files
- **Add to .gitignore**: Exclude sensitive files from version control
- **Encrypt When Possible**: Use encryption for stored credentials

### 4.2 Input Validation
- **Sanitize User Input**: Prevent injection attacks
- **Type Checking**: Validate data types
- **Boundary Checking**: Verify ranges and limits
- **Escape Special Characters**: In SQL, HTML, commands

## 5. Problem-Solving Framework

### 5.1 Analysis Phase
1. **Understand Requirements**: Clarify ambiguous requests
2. **Explore Codebase**: Read relevant files
3. **Identify Dependencies**: Check imports and requirements
4. **Plan Approach**: Break into smaller tasks

## 5A. Git Visual Commit Rules

### 5A.1 Mandatory Visual Display
- **ALWAYS** show branch graph after commits
- **ALWAYS** use visual tools: `python git_visual.py` or aliases
- **NEVER** commit without displaying visualization
- **ALWAYS** include graph in response when discussing commits

### 5A.2 Commit Workflow
```bash
# Required sequence
1. git add .
2. git commit -m "type(scope): description"
3. git graph -10  # MANDATORY - Show visual
4. git push origin branch-name
5. git graph --all  # MANDATORY - Show all branches
```

### 5A.3 Visual Aliases to Use
- `git graph` - Beautiful branch visualization
- `git tree` - Tree structure view  
- `git lg` - Colored log graph
- `git cv` - Commit with visual
- `git sg` - Status + graph
- `git pg` - Push + graph

### 5.2 Implementation Phase
1. **Incremental Changes**: Small, testable modifications
2. **Test Frequently**: Verify each change works
3. **Document Changes**: Update comments and docs
4. **Handle Edge Cases**: Consider boundary conditions

### 5.3 Debugging Protocol
1. **Reproduce Issue**: Understand the problem
2. **Add Logging**: Track variable states
3. **Isolate Problem**: Use binary search approach
4. **Fix Root Cause**: Not just symptoms

## 6. Project Management

### 6.1 File Structure
```
project/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration files
├── scripts/       # Utility scripts
└── README.md      # Project overview
```

### 6.2 Dependencies
- **Use Package Managers**: pip, npm, yarn
- **Pin Versions**: Specify exact versions in requirements
- **Virtual Environments**: Isolate project dependencies
- **Update Carefully**: Test after updates

## 7. Performance Guidelines

### 7.1 Optimization Priority
1. **Correctness**: Make it work
2. **Clarity**: Make it readable
3. **Performance**: Make it fast (if needed)

### 7.2 Best Practices
- **Avoid Premature Optimization**: Profile first
- **Use Built-in Functions**: They're usually optimized
- **Cache Results**: For expensive operations
- **Async Operations**: For I/O bound tasks

## 8. Testing Standards

### 8.1 Test Types
- **Unit Tests**: Test individual functions
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete workflows
- **Edge Cases**: Test boundary conditions

### 8.2 Test Coverage
- **Critical Paths**: 100% coverage
- **Business Logic**: >80% coverage
- **Utility Functions**: >70% coverage

## 9. Documentation Requirements

### 9.1 Code Documentation
- **Function Docstrings**: Parameters, returns, exceptions
- **Class Documentation**: Purpose and usage
- **Module Headers**: Brief description and author

### 9.2 Project Documentation
- **README.md**: Setup, usage, features
- **CHANGELOG.md**: Version history
- **API Documentation**: Endpoints and parameters
- **Architecture Docs**: System design decisions

## 10. Continuous Improvement

### 10.1 Learning
- **Save Patterns**: Store successful solutions in memory
- **Learn from Errors**: Document failure cases
- **Update Knowledge**: Adapt to new best practices

### 10.2 Feedback Loop
- **Track Success Rate**: Monitor task completion
- **Analyze Failures**: Understand root causes
- **Refine Approach**: Improve based on outcomes

## 11. User Interaction Principles

### 11.1 Collaboration
- **Respect Decisions**: User has final say
- **Provide Options**: Offer alternatives when appropriate
- **Explain Tradeoffs**: Clarify pros and cons
- **Stay Professional**: Maintain helpful tone

### 11.2 Progress Communication
- **Regular Updates**: For long-running tasks
- **Clear Status**: What's done, what's next
- **Error Reporting**: Explain what went wrong
- **Success Confirmation**: Verify task completion

## 12. Emergency Protocols

### 12.1 Critical Errors
1. **Stop Immediately**: Don't continue if unsafe
2. **Assess Damage**: Check what was affected
3. **Report Clearly**: Explain the issue
4. **Suggest Recovery**: Provide fix options

## 13. Git Visual Requirements

### 13.1 Every Commit Must:
- Display branch graph visualization
- Use semantic commit format: `type(scope): description`
- Show at least 10 commits in graph
- Include branch decorations and colors

### 13.2 Example Response Format:
```markdown
Committed your changes:

📊 Git Graph:
* a1b2c3d (HEAD -> feature/new) just now feat: add feature
* d4e5f6g (origin/main) 2 hours ago fix: bug fix

✅ Pushed to origin/feature/new
```

### 13.3 Tools to Use:
- `git_visual.py` - Interactive visual manager
- `GIT_VISUAL.bat` - Windows launcher
- Git aliases: graph, tree, lg, cv, sg, pg

### 12.2 Data Loss Prevention
- **Confirm Destructive Actions**: Double-check deletions
- **Create Backups**: Before major changes
- **Version Control**: Commit before risky operations
- **Test in Isolation**: Use test environments

---

## Priority Hierarchy

When rules conflict, follow this priority:
1. **Safety**: Protect user data and system
2. **Correctness**: Ensure functionality works
3. **Clarity**: Make code understandable
4. **Performance**: Optimize when necessary
5. **Elegance**: Refine implementation

## Update Log

- **Version 1.0**: Initial rules creation (2025-10-06)
- Rules should be reviewed and updated based on:
  - New security threats
  - Framework updates
  - User feedback
  - Performance metrics

---

*These rules ensure consistent, safe, and effective AI assistance for software development tasks.*
