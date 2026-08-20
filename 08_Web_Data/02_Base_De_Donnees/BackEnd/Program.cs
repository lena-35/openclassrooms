using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Autoriser le Front-end à communiquer avec le Back-end
builder.Services.AddCors(options => {
    options.AddPolicy("AutoriserFront", policy => {
        policy.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod();
    });
});

// Mets ton mot de passe root MySQL directement ici :
string connectionString = "server=localhost;database=foodly;uid=root;pwd=root;";

builder.Services.AddDbContext<FoodlyContext>(options =>
    options.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString)));

var app = builder.Build();

app.UseCors("AutoriserFront");

app.MapGet("/api/aliment", async (FoodlyContext db) => {
    return await db.Aliment.ToListAsync();
});

app.Run();