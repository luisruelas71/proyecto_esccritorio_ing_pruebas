using System;
using Crud.BusinessLayer;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace TestProductos
{
    [TestClass]
    public sealed class Test1
    {
        [TestMethod]
        public void RechazaNombreVacio()
        {
            ProductoBL productoBL = new ProductoBL();

            Assert.Throws<Exception>(
                () => productoBL.validarNombre(string.Empty));
        }
    }
}
