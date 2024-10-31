using System.Collections.Generic;

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

List<Stone> repo = new List<Stone>();
{
    new(1, "defolt stone", "stone");
    new(2, "Ìנאלמנ", "stone");
    new(3, "‗רלא", "stone");
}
app.MapGet("/", () => repo);
app.MapPost("/", (Stone x) => repo.Add(x));
app.Run();

class Stone
{
    int number;
    string name;
    string type;

    public Stone(int number, string name, string type)
    {
        Number = number;
        Name = name;
        Type = type;
    }
    public int Number { get => number; set => number = value; }
    public string Name { get => name; set => name = value; }
    public string Type { get => type; set => type = value; }
}