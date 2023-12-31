import React from "react";
import { NavLink } from "react-router-dom";
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

export default function NavbarApp({ user, setUser }){

    const handleLogout = () => {
        fetch("/logout", {
          method: "DELETE",
        })
        .then((res) => {
            if (res.ok) {
                setUser('')
            }
        })
      }

    return (
        <header> 
            <Navbar className='nav-bar'>
                <Container>
                    <NavLink to='/journal' className='navbar-button'> Journal </NavLink>
                    <NavLink to='/mood' className='navbar-button'> Mood Tracking </NavLink> 
                    <NavLink to="/meditate" className='navbar-button'> Meditate </NavLink> 
                    {user ? <NavLink to='/account' className='navbar-button'> Manage Account </NavLink> : null}
                    {user ? <Button onClick={handleLogout} className='logout-button'> Logout </Button> : <NavLink to='/login' className='login-button'> Login/Register </NavLink>}
                </Container>
            </Navbar>
        </header>
    )
}
