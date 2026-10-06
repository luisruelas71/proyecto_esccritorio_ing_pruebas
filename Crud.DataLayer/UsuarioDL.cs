using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Crud.DataLayer
{
    public class UsuarioDL
    {
        private readonly string connectionString =
            "server=localhost;port=3306;database=ferreteria;uid=root;pwd=Root;SslMode=Disabled;AllowPublicKeyRetrieval=True;";

        public void altaUsuario(int IdUsuario, string Nombre, string ApellidoPaterno, string ApellidoMaterno, string NombreUsuario, string Contrasena)
        {
            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "INSERT INTO usuario (id_usuario, nombre, apellido_paterno, apellido_materno, nombre_usuario, contrasena) VALUES (@IdUsuario, @Nombre, @ApellidoPaterno, @ApellidoMaterno, @NombreUsuario, @Contrasena)";
                MySqlCommand cmd = new MySqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@IdUsuario", IdUsuario);
                cmd.Parameters.AddWithValue("@Nombre", Nombre);
                cmd.Parameters.AddWithValue("@ApellidoPaterno", ApellidoPaterno);
                cmd.Parameters.AddWithValue("@ApellidoMaterno", ApellidoMaterno);
                cmd.Parameters.AddWithValue("@NombreUsuario", NombreUsuario);
                cmd.Parameters.AddWithValue("@Contrasena", Contrasena);

                conn.Open();
                cmd.ExecuteNonQuery();

            }
        }

        public void bajaUsuario(int IdUsuario)
        {
            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "DELETE FROM usuario WHERE id_usuario=@IdUsuario";
                MySqlCommand cmd = new MySqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@IdUsuario", IdUsuario);

                conn.Open();
                cmd.ExecuteNonQuery();
            }
        }

        public Usuario consultaUsuario(int IdUsuario)
        {
            Usuario usuario = null;

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "SELECT id_usuario, nombre, apellido_paterno, apellido_materno, nombre_usuario " +
                               "FROM usuario WHERE id_usuario=@IdUsuario";

                MySqlCommand cmd = new MySqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@IdUsuario", IdUsuario);

                conn.Open();

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        usuario = new Usuario
                        {
                            IdUsuario = Convert.ToInt32(reader["id_usuario"]),
                            Nombre = reader["nombre"].ToString(),
                            ApellidoPaterno = reader["apellido_paterno"].ToString(),
                            ApellidoMaterno = reader["apellido_materno"].ToString(),
                            NombreUsuario = reader["nombre_usuario"].ToString()
                        };
                    }
                }
            }

            return usuario;
        }


        public void modificacionUsuario(int IdUsuario, string Nombre, string ApellidoPaterno, string ApellidoMaterno, string NombreUsuario, string Contrasena)
        {
            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                string query = "UPDATE usuario SET nombre=@Nombre, apellido_paterno=@ApellidoPaterno, apellido_materno=@ApellidoMaterno, nombre_usuario=@NombreUsuario, contrasena=@Contrasena WHERE id_usuario=@IdUsuario"; MySqlCommand cmd = new MySqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@IdUsuario", IdUsuario);
                cmd.Parameters.AddWithValue("@Nombre", Nombre);
                cmd.Parameters.AddWithValue("@ApellidoPaterno", ApellidoPaterno);
                cmd.Parameters.AddWithValue("@ApellidoMaterno", ApellidoMaterno);
                cmd.Parameters.AddWithValue("@NombreUsuario", NombreUsuario);
                cmd.Parameters.AddWithValue("@Contrasena", Contrasena);

                conn.Open();
                cmd.ExecuteNonQuery();
            }
        }


        public List<Usuario> obtenerTodosUsuarios()
        {
            List<Usuario> lista = new List<Usuario>();

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                conn.Open();
                string query = @"SELECT 
                            id_usuario,
                            nombre,
                            apellido_paterno,
                            apellido_materno,
                            nombre_usuario
                        FROM usuario";

                using (MySqlCommand cmd = new MySqlCommand(query, conn))
                {
                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Usuario u = new Usuario
                            {
                                IdUsuario = reader.GetInt32("id_usuario"),
                                Nombre = reader.GetString("nombre"),
                                ApellidoPaterno = reader.GetString("apellido_paterno"),
                                ApellidoMaterno = reader.IsDBNull(reader.GetOrdinal("apellido_materno")) ? "" : reader.GetString("apellido_materno"),
                                NombreUsuario = reader.GetString("nombre_usuario")
                            };
                            lista.Add(u);
                        }
                    }
                }
            }

            return lista;
        }

        public bool ExisteUsuario(int idUsuario)
        {
            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                conn.Open();
                string query = "SELECT COUNT(*) FROM usuario WHERE id_usuario = @id";
                using (MySqlCommand cmd = new MySqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@id", idUsuario);
                    int count = Convert.ToInt32(cmd.ExecuteScalar());
                    return count > 0;
                }
            }
        }
    }
}
