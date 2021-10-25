import "./Header.css"
import { Icon } from '@iconify/react';

function Header() {
  return (
    <div className="header">
      <h1>UNIStats</h1>

      <form>
        <Icon icon="akar-icons:search" />
        <input type="text" />
      </form>
    </div>
  )
}

export default Header;