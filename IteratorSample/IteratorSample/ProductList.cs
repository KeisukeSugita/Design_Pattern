using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    public class ProductList
    {
        private List<Product> products = new List<Product>();

        public void Add(Product product)
        {
            products.Add(product);
        }

        public Product GetProduct(int index)
        {
            return products[index];
        }

        public int GetCount()
        {
            return products.Count;
        }
    }
}
