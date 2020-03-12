using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    public class ProductListIterator : IProductListIterator
    {
        private MyProductList products;
        private int index;

        public ProductListIterator(MyProductList products)
        {
            this.products = products;
            this.index = 0;
        }

        public bool hasNext()
        {
            return products.GetCount() > index ? true : false;
        }

        public Product Next()
        {
            Product product = products.GetProduct(index);
            index++;
            return product;
        }
    }
}
