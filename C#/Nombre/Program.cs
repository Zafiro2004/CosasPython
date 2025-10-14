// Solicita el nombre y los apellidos por separado
Console.Write("Introduce tu nombre: ");
string nombre = Console.ReadLine();

Console.Write("Introduce tu primer apellido: ");
string primerApellido = Console.ReadLine();

Console.Write("Introduce tu segundo apellido: ");
string segundoApellido = Console.ReadLine();

// Saluda al usuario con el nombre completo
Console.WriteLine($"¡Hola, {nombre} {primerApellido} {segundoApellido}!");
