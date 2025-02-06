using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Http;
using System.IO;
using System.Linq;

[ApiController]
[Route("api/pessoas")]
public class PessoasController : ControllerBase
{
    private readonly AppDbContext _context;

    public PessoasController(AppDbContext context)
    {
        _context = context;
    }

    // Endpoint para importar dados do CSV com arquivo anexado
    [HttpPost("importar")]
    public async Task<IActionResult> ImportarCSV(IFormFile file)
    {
        if (file == null || file.Length == 0)
        {
            return BadRequest("Nenhum arquivo foi enviado.");
        }

        // Verificar se o arquivo tem a extensão CSV
        if (Path.GetExtension(file.FileName).ToLower() != ".csv")
        {
            return BadRequest("Verifique se o arquivoe está em CSV.");
        }

        // Processando o arquivo CSV
        using (var reader = new StreamReader(file.OpenReadStream()))
        {
            var linhas = await reader.ReadToEndAsync();
            var pessoas = linhas.Split('\n').Skip(1).Select(l => l.Split(',')).Select(c => new Pessoa
            {
                Id = int.Parse(c[0]),
                Nome = c[1],
                Idade = int.Parse(c[2]),
                Cidade = c[3],
                Profissao = c[4]
            }).ToList();

            await _context.Pessoas.AddRangeAsync(pessoas);
            await _context.SaveChangesAsync();
        }

        return Ok("Importação concluída com sucesso.");
    }

    // Endpoint para consultar uma pessoa pelo ID
    [HttpGet("{id}")]
    public async Task<IActionResult> GetPessoa(int id)
    {
        var pessoa = await _context.Pessoas.FindAsync(id);
        return pessoa == null ? NotFound() : Ok(pessoa);
    }
}
