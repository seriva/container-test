using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace hello.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class HelloController : ControllerBase
    {

        private readonly ILogger<HelloController> _logger;

        public HelloController(ILogger<HelloController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public HelloMessage Get()
        {
            return new HelloMessage
            {
                message = "Hello, world!"
            };
        }
    }
}
