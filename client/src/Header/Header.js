import "./Header.css"
import { Icon } from '@iconify/react';

function Header() {
  return (
    <div className="header">
      <h1>UNIStats</h1>

      <form>
        <Icon icon="akar-icons:search" width="0.8vw" color="#575757"/>
        <input type="text" placeholder="Search University"/>
      </form>
    </div>
  )
}

export default Header;