import "./Header.css"
import { Icon } from '@iconify/react';

function Header() {
  return (
    <div className="header">
      <h1>UNIStats</h1>

      <section>
        <p>All Stats</p>

        <p>Add Stat</p>

        <p>Account</p>
      </section>
    </div>
  )
}

export default Header;