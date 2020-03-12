using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    class IteratorMain
    {
        public static void Main()
        {
            var employee = new Employee();
            employee.createProductList();
            employee.readProducts();
        }
    }
}
