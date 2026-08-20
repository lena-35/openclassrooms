using Microsoft.EntityFrameworkCore;

public class Aliment
{
    public int Id { get; set; }
    public required string Nom { get; set; }
    public int Calories { get; set; }
}

public class FoodlyContext : DbContext
{
    public FoodlyContext(DbContextOptions<FoodlyContext> options) : base(options) { }

    public DbSet<Aliment> Aliment { get; set; }
}