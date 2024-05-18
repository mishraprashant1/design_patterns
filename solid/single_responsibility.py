"""
A class should have only one reason to change.

The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning that a
class should have only one job or responsibility. This principle helps to keep classes focused and makes them easier to
understand, maintain, and test.

When a class has multiple responsibilities, it becomes tightly coupled to different parts of the system, making it
difficult to change one responsibility without affecting the others. By separating these responsibilities into  separate
classes, you can achieve better modularity and flexibility in your code.

Let's explore the Single Responsibility Principle with an example:

Real-Life Example Problem:

Imagine you're working on a user management system that allows users to register, log in, and update their profiles. You
have a User class that handles all these operations, including database interactions, input validation, and sending
notifications. This class is becoming too complex and difficult to maintain.

Solution with the Single Responsibility Principle:

To apply the Single Responsibility Principle, you can refactor the User class into multiple classes, each with a single
responsibility:

User: This class represents the user entity and contains user-specific data and methods related to the user's profile.

UserRepository: This class is responsible for database interactions, such as saving, updating, and retrieving user data.

UserValidator: This class handles input validation for user data, ensuring that the data is valid before saving it to
the database.

UserNotifier: This class is responsible for sending notifications to users, such as welcome emails or password reset
notifications.

By separating these responsibilities into separate classes, you can achieve better separation of concerns and make your
code easier to maintain and extend.

Benefits of the Single Responsibility Principle:

1. Improved Modularity: By separating responsibilities into separate classes, you can achieve better modularity in your
code, making it easier to understand, maintain, and extend.

2. Easier Testing: Classes with a single responsibility are easier to test because you can focus on testing specific

3. Better Code Organization: The Single Responsibility Principle helps you organize your code more effectively by
separating concerns and keeping classes focused on a single job.

4. Reduced Coupling: Classes with a single responsibility are less coupled to other parts of the system, making them
easier to change and maintain.

5. Improved Re-usability: Classes with a single responsibility are more reusable because they are focused on a specific
task and can be used in different contexts.

By following the Single Responsibility Principle, you can create more maintainable, flexible, and testable code that is
easier to understand and extend.
"""

# Single Responsibility Principle Example

from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# Above is a bad example of the Single Responsibility Principle because the FileManager class has multiple
# responsibilities: reading and writing files, as well as compressing and decompressing files. This violates the Single
# Responsibility Principle because the class has more than one reason to change.

# Refactored Example:

class FileReaderWriter:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# In the refactored example, we have separated the responsibilities of reading/writing files and
# compressing/decompressing files into two separate classes: FileReaderWriter and ZipFileManager. This separation
# adheres to the Single Responsibility Principle, making the classes more focused and easier to maintain.
