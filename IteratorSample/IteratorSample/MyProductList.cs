using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    public class MyProductList : ProductList, IMyProductList
    {
        public IProductListIterator GetIterator()
        {
            return new ProductListIterator(this);
        }
    }
}
