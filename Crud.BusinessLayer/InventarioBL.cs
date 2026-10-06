using Crud.EntityLayer;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;

namespace Crud.BusinessLayer
{
    public class InventarioBL
    {
        // 1. Cadena de conexión corregida con SslMode=Disabled para MySQL 9
        private readonly string connectionString =
            "Server=localhost;Port=3306;Database=ferreteria;Uid=root;Pwd=Root;SslMode=Disabled;AllowPublicKeyRetrieval=True;";

        public List<Producto> mostrarInventario()
        {
            List<Producto> inventario = new List<Producto>();

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "SELECT Nombre, Categoria, Cantidad FROM producto";
                MySqlCommand cmd = new MySqlCommand(query, conn);
                conn.Open();

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        inventario.Add(new Producto
                        {
                            Nombre = reader["Nombre"].ToString(),
                            Categoria = reader["Categoria"].ToString(),
                            Cantidad = Convert.ToInt32(reader["Cantidad"])
                        });
                    }
                }
            }

            return inventario;
        }

        public List<Inventario> mostrarEntradas()
        {
            List<Inventario> entradas = new List<Inventario>();

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "SELECT Cantidad FROM producto";
                MySqlCommand cmd = new MySqlCommand(query, conn);
                conn.Open();

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        entradas.Add(new Inventario
                        {
                            Cantidad = Convert.ToInt32(reader["Cantidad"])
                        });
                    }
                }
            }

            return entradas;
        }

        public List<Inventario> mostrarSalidas()
        {
            List<Inventario> salidas = new List<Inventario>();

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "SELECT Cantidad FROM producto";
                MySqlCommand cmd = new MySqlCommand(query, conn);
                conn.Open();

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        salidas.Add(new Inventario
                        {
                            Cantidad = Convert.ToInt32(reader["Cantidad"])
                        });
                    }
                }
            }

            return salidas;
        }
    }
}