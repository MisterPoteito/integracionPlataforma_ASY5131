using Microsoft.AspNetCore.Mvc;

namespace Hola.Controller
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClienteController : ControllerBase
    {

        private static IList<Cliente> _clientes = new List<Cliente>()
    {};

        // GET: api/clientes
        [HttpGet]
        public IEnumerable<Cliente> Get()
        {
            return _clientes;
        }

        // GET: api/clientes/{Rut}
        [HttpGet("{Rut}")]
        public Cliente Get(int Rut)
        {
            Cliente resultado = _clientes.FirstOrDefault(c => c.Rut == Rut);
            return resultado;
        }

        // POST: api/clientes
        [HttpPost]
        public IActionResult Post([FromBody] Cliente cliente)
        {
            if (_clientes.Any(c => c.Rut == cliente.Rut))
            {
                return BadRequest("Ya existe un cliente con el mismo RUT.");
            }

            _clientes.Add(cliente);
            return CreatedAtAction(nameof(Cliente), new { rut = cliente.Rut }, cliente);
        }

        // PUT: api/clientes/{Rut}
        [HttpPut("{Rut}")]
        public void Put(int Rut, [FromBody] Cliente cliente)
        {
            var clienteExistente = _clientes.FirstOrDefault(c => c.Rut == Rut);
            if (clienteExistente != null)
            {
                clienteExistente.Nombre = cliente.Nombre;
                clienteExistente.Apellido = cliente.Apellido;
            }
            if (clienteExistente == null)
            {
                _clientes.Add(cliente);
            }
            else
            {
                _clientes.Remove(clienteExistente);
                _clientes.Add(cliente);
            }
        }

        // DELETE: api/clientes/{Rut}
        [HttpDelete("{Rut}")]
        public void Delete(int Rut)
        {
                _clientes.Remove(_clientes.FirstOrDefault(c => c.Rut == Rut));
        }
    }
}
