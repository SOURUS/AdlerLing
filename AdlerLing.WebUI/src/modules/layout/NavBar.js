import React from 'react';
import { Menu, Icon, Sidebar, Segment, Header, Image } from 'semantic-ui-react';
import { NavLink } from 'react-router-dom';

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = { menuVisible: false };
    }

    render() {
        return (
            <Menu vertical fixed inverted >
                <Menu.Menu>
                    <Menu.Item>Personal account</Menu.Item>
                </Menu.Menu>

                <Menu.Menu>
                    <Menu.Item>Irregular verbs</Menu.Item>
                </Menu.Menu>

                <Menu.Menu>
                    <Menu.Item as={NavLink} to='/signup'>Sign up</Menu.Item>
                </Menu.Menu>

                <Menu.Menu>
                    <Menu.Item as={NavLink} to='/login'>Login</Menu.Item>
                </Menu.Menu>
            </Menu>
        );
    };
};

export default NavBar;