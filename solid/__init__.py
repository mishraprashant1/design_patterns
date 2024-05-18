"""

1. Single-responsibility principle (SRP)
2. Open–closed principle (OCP)
3. Liskov substitution principle (LSP)
4. Interface segregation principle (ISP)
5. Dependency inversion principle (DIP)


Summary:
1. Single-responsibility principle (SRP): A class should have only one reason to change, meaning it should have only one
responsibility or job.
2. Open–closed principle (OCP): Software entities should be open for extension but closed for modification, meaning they
should allow new functionality to be added without changing existing code.
3. Liskov substitution principle (LSP): Objects of a superclass should be replaceable with objects of its subclasses without
affecting the correctness of the program.
4. Interface segregation principle (ISP): Clients should not be forced to depend on interfaces they do not use, meaning
interfaces should be specific to the client's needs.
5. Dependency inversion principle (DIP): High-level modules should not depend on low-level modules, but both should depend
on abstractions, meaning classes should depend on abstractions rather than concrete implementations.

Questions to ask for each principle:
1. Single-responsibility principle (SRP):
- Does the class have only one reason to change?
- Does the class have only one responsibility or job?
2. Open–closed principle (OCP):
- Is the software entity open for extension?
- Is the software entity closed for modification?
3. Liskov substitution principle (LSP):
- Can objects of a subclass be replaced with objects of its superclass without affecting the program?
4. Interface segregation principle (ISP):
- Do we have fat interfaces with unnecessary methods?
5. Dependency inversion principle (DIP):
- Are high-level modules depending on low-level modules? Like Payment Service depending on Payment Processor.
"""