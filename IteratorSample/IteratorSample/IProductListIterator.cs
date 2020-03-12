using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorSample
{
    public interface IProductListIterator
    {
        bool hasNext();
        Product Next();
    }
}
