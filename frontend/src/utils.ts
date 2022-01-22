import jwt_decode from 'jwt-decode';
import { IJWTData } from './interfaces/auth';

export const getLocalToken = () => localStorage.getItem('token');

export const saveLocalToken = (token: string) =>
  localStorage.setItem('token', token);

export const removeLocalToken = () => localStorage.removeItem('token');

export const hasPermission = (token: string, permission: string) => {
  if (!token) {
    return false;
  }
  try {
    const decoded = jwt_decode<IJWTData>(token);
    return decoded.superuser || decoded.permissions.includes(permission);
  } catch (error) {
      removeLocalToken();
      return false;
  }
};
