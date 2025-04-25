import express from "express";
import clientesRoutes from "./modules/clientes/clientes.routes";
import cotizacionRoutes from "./modules/cotizacion/cotizacion.routes";
import trackingRoutes from "./modules/tracking/tracking.routes";
import embarqueRoutes from "./modules/embarque/embarque.routes";
import facturacionRoutes from "./modules/facturacion/facturacion.routes";
import usuariosRoutes from "./modules/usuarios/usuarios.routes";
import baseDatosRoutes from "./modules/base-datos/baseDatos.routes";

const app = express();
app.use(express.json());

// Rutas
app.use("/api/clientes", clientesRoutes);
app.use("/api/cotizaciones", cotizacionRoutes);
app.use("/api/tracking", trackingRoutes);
app.use("/api/embarques", embarqueRoutes);
app.use("/api/facturacion", facturacionRoutes);
app.use("/api/usuarios", usuariosRoutes);
app.use("/api/base-datos", baseDatosRoutes);

export default app;