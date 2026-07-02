import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/Login";
import AdminDashboard from "../pages/AdminDashboard";
import TeacherDashboard from "../pages/TeacherDashboard";
import StudentDashboard from "../pages/StudentDashboard";

import ProtectedRoute from "./ProtectedRoute";

import AuthLayout from "../layouts/AuthLayout";
import DashboardLayout from "../layouts/DashboardLayout";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        {/* =========================
            Public Routes
        ========================== */}
        <Route element={<AuthLayout />}>
          <Route path="/" element={<Navigate to="/login" replace />} />
          <Route path="/login" element={<Login />} />
        </Route>

        {/* =========================
            Admin Routes
        ========================== */}
        <Route element={<ProtectedRoute requiredRole="admin" />}>
          <Route element={<DashboardLayout />}>
            <Route
              path="/admin-dashboard"
              element={<AdminDashboard />}
            />
          </Route>
        </Route>

        {/* =========================
            Teacher Routes
        ========================== */}
        <Route element={<ProtectedRoute requiredRole="teacher" />}>
          <Route element={<DashboardLayout />}>
            <Route
              path="/teacher-dashboard"
              element={<TeacherDashboard />}
            />
          </Route>
        </Route>

        {/* =========================
            Student Routes
        ========================== */}
        <Route element={<ProtectedRoute requiredRole="student" />}>
          <Route element={<DashboardLayout />}>
            <Route
              path="/student-dashboard"
              element={<StudentDashboard />}
            />
          </Route>
        </Route>

        {/* =========================
            Unknown Routes
        ========================== */}
        <Route
          path="*"
          element={<Navigate to="/login" replace />}
        />

      </Routes>
    </BrowserRouter>
  );
}