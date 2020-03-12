using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    public class Employee
    {
        private MyProductList products = new MyProductList();
        public void createProductList()
        {
            products.Add(new Product(0001, "お菓子", 150));
            products.Add(new Product(0002, "洋服", 5000));
            products.Add(new Product(0003, "ゲーム", 10000));
        }

        public void readProducts()
        {
            IProductListIterator productListIterator = products.GetIterator();
            while (productListIterator.hasNext())
            {
                Product product = productListIterator.Next();
                Console.WriteLine($"{product.Name}は{product.Price}円です。");
            }
        }
    }
}
