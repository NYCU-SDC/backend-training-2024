# Assignments

How to add your assignment as a submodule:
1. Fork this repository and clone it to your local machine.
2. Create your own assignment repository (if you haven't already).
3. Navigate to the `members/` directory.
4. Add your assignment repository as a submodule:
    ```bash
    git submodule add <your-repo-url> members/<your-github-id>
    ```
5. Commit the changes:
    ```bash
    git commit -m "Add <your-github-id> assignment"
    ```
6. Push your changes to your forked repository.
7. Create a Pull Request to the main repository.