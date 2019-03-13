import React from 'react';
import { Layout, Menu, Icon } from 'antd';
import { NavLink, withRouter } from 'react-router-dom';

const { Sider } = Layout;

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = { collapsed: false, location: props.location };
    }

    onCollapse = (collapsed) => {
        this.setState({ collapsed });
    }

    render() {
        return (
            <Sider
                collapsible
                collapsed={this.state.collapsed}
                onCollapse={this.onCollapse.bind(this)}
            >
                <div className="logo" />
                <Menu theme="dark" defaultSelectedKeys={[this.state.location.pathname]} mode="inline">
                    <Menu.Item key="/account">
                        <NavLink to="/">
                            <Icon type="user" />
                            <span>Personal account</span>
                        </NavLink>
                    </Menu.Item>
                    <Menu.Item key="/">
                        <NavLink to="/">
                            <Icon type="appstore" />
                            <span>Irregular verbs</span>
                        </NavLink>
                    </Menu.Item>
                    <Menu.Item key="/signup">
                        <NavLink to="/signup">Sign up</NavLink>
                    </Menu.Item>
                    <Menu.Item key="/login">
                        <NavLink to="/login">
                            <Icon type="pie-chart" />
                            <span>Login</span>
                        </NavLink>
                    </Menu.Item>
                </Menu>
            </Sider>
        );
    };
};

export default withRouter(NavBar);