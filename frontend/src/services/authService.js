import axios from "axios";

const STORAGE_KEYS = {
  token: "attendance_auth_token",
  user: "attendance_auth_user",
};

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

const normalizeError = (error) => {
  if (error?.response?.data) {
    if (typeof error.response.data === "string") {
      return error.response.data;
    }

    if (typeof error.response.data === "object") {
      return (
        error.response.data.message ||
        error.response.data.detail ||
        error.response.data.error ||
        error.response.data.non_field_errors?.[0] ||
        "Authentication failed"
      );
    }
  }

  if (error?.message) {
    return error.message;
  }

  return "Authentication failed";
};

export const setAuthSession = (authData) => {
  const payload = authData?.data ?? authData;
  const token = payload?.accessToken || payload?.token || payload?.access || payload?.jwt || null;
  const user = payload?.user || payload?.profile || payload?.data?.user || null;

  if (token) {
    localStorage.setItem(STORAGE_KEYS.token, token);
  }

  if (user) {
    localStorage.setItem(STORAGE_KEYS.user, JSON.stringify(user));
  }

  return { token, user };
};

export const clearAuthSession = () => {
  localStorage.removeItem(STORAGE_KEYS.token);
  localStorage.removeItem(STORAGE_KEYS.user);
};

export const login = async (credentials) => {
  try {
    const response = await api.post("/accounts/login/", credentials);
    const authData = setAuthSession(response.data);

    return {
      ...response.data,
      token: authData.token,
      user: authData.user,
    };
  } catch (error) {
    clearAuthSession();
    throw new Error(normalizeError(error));
  }
};

export const logout = () => {
  clearAuthSession();
};

export const getAuthToken = () => localStorage.getItem(STORAGE_KEYS.token);

export const getCurrentUser = () => {
  const storedUser = localStorage.getItem(STORAGE_KEYS.user);

  if (!storedUser) {
    return null;
  }

  try {
    return JSON.parse(storedUser);
  } catch {
    return null;
  }
};

export const isAuthenticated = () => Boolean(getAuthToken());

export const getAuthHeaders = () => {
  const token = getAuthToken();

  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const getDashboardPath = (user = getCurrentUser()) => {
  const role = user?.role?.toLowerCase() || user?.userType?.toLowerCase() || "";

  if (role === "admin") return "/admin-dashboard";
  if (role === "teacher") return "/teacher-dashboard";
  if (role === "student") return "/student-dashboard";

  return "/login";
};

const authService = {
  login,
  logout,
  getAuthToken,
  getCurrentUser,
  isAuthenticated,
  getAuthHeaders,
  getDashboardPath,
};

export default authService;
